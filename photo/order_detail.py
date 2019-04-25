from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from photo.auth import login_required
from photo.db import get_db

bp = Blueprint('order_detail', __name__)
def get_order(id, check_author=True):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT ord.orderid orderid, ord.startdate startdate,"
        " ord.status status, ord.expectduration expectduration,"
        " ord.price price, ord.place place, ord.ordertype ordertype, ord.description description,"
        " ord.satisfaction satisfaction, ma.username managername"
        " FROM porder ord, projectmanager ma"
        " WHERE ord.orderid = '%d' AND"
        " ord.managerid = ma.id" % (id, )
    )
    order = cursor.fetchone()

    if order is None:
        abort(404, "Order id {0} doesn't exist.".format(id))

    # if check_author and post['author_id'] != g.user['id']:
    #     abort(403)

    return order

def get_photographers(id, check_author=True):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT photo.id id, photo.username name, photo.level level, MAX(pp.phone) phone"
        " FROM photographer photo, photographer_phone pp"
        " WHERE photo.id = pp.id AND"
        " photo.id in (SELECT photographerid"
        "               FROM takephoto"
        "               WHERE orderid =  '%d')"
        " GROUP BY photo.id, photo.username, photo.level" % (id, )
    )
    photographers = cursor.fetchall()
    return photographers

def get_aftereffects(id, check_author=True):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT effect.id id, effect.username name, effect.level level, MAX(ap.phone) phone"
        " FROM aftereffect effect, aftereffect_phone ap"
        " WHERE effect.id = ap.id AND"
        " effect.id in (SELECT effectid"
        "               FROM doeffect"
        "               WHERE orderid =  '%d')"
        " GROUP BY effect.id, effect.username, effect.level" % (id, )
    )
    aftereffects = cursor.fetchall()

    return aftereffects

def get_all_name(position):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT username FROM %s " % (position, )
    )
    names = cursor.fetchall()

    return names

def order_check(id=-1):
    error = None
    flag = False
    if request.method == 'POST':
        status = request.form['status']
        startdate = request.form['startdate']
        expectduration = request.form['expectduration']
        price = request.form['price']
        ordertype = request.form['ordertype']
        managername = request.form['managername']
        description = request.form['description']
        photographernames = request.form.getlist('photographer_name')
        aftereffectnames = request.form.getlist('aftereffect_name')
        status = str(status)
        startdate = str(startdate)
        expectduration = int(expectduration)
        price = int(price)
        ordertype = str(ordertype)
        managername = str(managername)
        description = str(description)
        ordertype = ordertype.lower()
        error = None
        flag = True
        if not status or not startdate or not expectduration or not price \
            or not ordertype or not managername or not photographernames or \
            not aftereffectnames or not description:
            error = 'Basic information is not complete.'
        if not photographernames or not aftereffectnames:
            error = 'Photographer and aftereffect information is not complete.'


        if ordertype != 'wedding' and ordertype != 'art' and ordertype != 'business':
            error = 'This order type does not exist'

        if expectduration > 1000:
            error = 'Expect duration is larger than 1000 days'
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id from projectmanager WHERE username = '%s'" % (managername,))
        manager = cursor.fetchone()


        if manager is None:
            error = 'Incorrect manager'
            
        if error is not None:
            # flash(error)
            flag =  False
        else:
            flag = True
            managerid = manager['id']
            managerid = int(managerid)
            if id == -1:
                cursor.execute(
                    "INSERT INTO porder(startdate, status, expectduration, price, ordertype, managerid)"
                    "VALUES ('%s', '%s', '%d', '%d', '%s', '%d');"
                     % \
                    (startdate, status, expectduration, price, ordertype, managerid))
                cursor.execute(" SELECT orderid FROM porder ORDER BY orderid DESC")
                return_order = cursor.fetchone()
                id = return_order['orderid']
            if id != -1:
                cursor.execute(
                    "UPDATE porder SET startdate = '%s', status = '%s',"
                    " expectduration = '%d', price = '%d', ordertype = '%s',"
                    " managerid = '%d', description = '%s'"
                    " WHERE orderid = '%d'" % \
                    (startdate, status, expectduration, price, ordertype, managerid, description, id)
                )
                cursor.execute(
                    "DELETE FROM takephoto WHERE orderid = '%d'" % (id,))
                cursor.execute(
                    "DELETE FROM doeffect WHERE orderid = '%d'" % (id,))
                for photographername in photographernames:
                    cursor.execute(
                        "SELECT id FROM photographer WHERE username = '%s'" % (photographername)
                    )
                    photographerid = cursor.fetchone()
                    cursor.execute(
                        "INSERT INTO takephoto(orderid, photographerid) VALUES ('%d', '%d')" % (id, photographerid['id'])
                    )
                    
                for aftereffectname in aftereffectnames:
                    cursor.execute(
                        "SELECT id FROM aftereffect WHERE username = '%s'" % (aftereffectname)
                    )
                    aftereffectid = cursor.fetchone()
                    cursor.execute(
                        "INSERT INTO doeffect(orderid, effectid) VALUES ('%d', '%d')" % (id, aftereffectid['id'])
                    )
                db.commit()
    return flag, error, id


@bp.route('/<int:id>/order_detail/index')
def index(id):
    # print(id)
    if (g.user):
        g.current = "index"
        order = get_order(id)
        photographers = get_photographers(id)
        aftereffects = get_aftereffects(id)

        return render_template('order_detail/detail_index.html', order=order, photographers=photographers, \
            aftereffects = aftereffects)

    else:
        return redirect(url_for('auth.login'))

@bp.route('/order_detail/detail_create', methods=('GET', 'POST'))
@login_required
def detail_create():
    status, error, id = order_check()
    photographer_names = get_all_name('photographer')
    aftereffect_names = get_all_name('aftereffect')
    projectmanager_names = get_all_name('projectmanager')
    if status == True:
        return redirect(url_for('order_detail.index', order=None, photographers=None, \
        aftereffects = None, id = id))
    return render_template('order_detail/detail_create.html', order=None, photographers=None, \
            aftereffects=None, photographer_names=photographer_names, aftereffect_names=aftereffect_names, \
            projectmanager_names = projectmanager_names, error = error)

# @bp.route('/basic_info/', methods=('GET', 'POST'))
# @login_required
# def basic_info():
#     status, error = order_check()
#     photographer_names = get_all_name('photographer')
#     aftereffect_names = get_all_name('aftereffect')
#     projectmanager_names = get_all_name('projectmanager')
#     if status == True:
#         # return redirect(url_for('order_detail.index', order=None, photographers=None, \
#         # aftereffects = None, id = id))
#         return render_template('order_detail/detail_create.html', order=None, photographers=None, \
#                 aftereffects=None, photographer_names=photographer_names, aftereffect_names=aftereffect_names, \
#                 projectmanager_names = projectmanager_names, error = error)



@bp.route('/<int:id>/order_detail/detail_update', methods=('GET', 'POST'))
@login_required
def detail_update(id):
    order = get_order(id)
    photographer_names = get_all_name('photographer')
    aftereffect_names = get_all_name('aftereffect')
    photographers = get_photographers(id)
    aftereffects = get_aftereffects(id)
    status, error, id_two= order_check(id)
    projectmanager_names = get_all_name('projectmanager')
    if status == True:
        return redirect(url_for('order_detail.index', order=order, photographers=photographers, \
        aftereffects = aftereffects, id = id))

    return render_template('order_detail/detail_update.html', order=order, photographers=photographers, \
            aftereffects=aftereffects, projectmanager_names=projectmanager_names, \
            photographer_names=photographer_names, aftereffect_names=aftereffect_names, error = error)

            
@bp.route('/<int:id>/detail_delete', methods=('POST',))
@login_required
def delete(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM porder WHERE orderid = '%d'" % (id,))
    db.commit()
    return redirect(url_for('dashboard.index'))