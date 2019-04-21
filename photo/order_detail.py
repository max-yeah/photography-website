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
        " ord.price price, ord.place place, ord.ordertype ordertype,"
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


@bp.route('/order_detail/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO post (title, body, author_id)"
                " VALUES ('%s', '%s', '%d')" % \
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('order_detail.index'))

    return render_template('order_detail/create.html')



@bp.route('/<int:id>/order_detail/detail_update', methods=('GET', 'POST'))
@login_required
def detail_update(id):
    order = get_order(id)
    photographers = get_photographers(id)
    aftereffects = get_aftereffects(id)
    if request.method == 'POST':
        status = request.form['status']
        startdate = request.form['startdate']
        expectduration = request.form['expectduration']
        price = request.form['price']
        ordertype = request.form['ordertype']
        managername = request.form['managername']
        status = str(status)
        startdate = str(startdate)
        expectduration = int(expectduration)
        price = int(price)
        ordertype = str(ordertype)
        managername = str(managername)
        ordertype = ordertype.lower()
        error = None

        if not status or not startdate or not expectduration or not price \
            or not ordertype or not managername:
            error = 'Information is not complete.'
        if ordertype != 'wedding' and ordertype != 'art' and ordertype != 'business':
            error = 'This order type does not exist'

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id from projectmanager WHERE username = '%s'" % (managername,))
        manager = cursor.fetchone()
        managerid = manager['id']
        managerid = int(managerid)

        if managerid is None:
            error = 'Incorrect manager'
            
        if error is not None:
            flash(error)
        else:
            cursor.execute(
                "UPDATE porder SET startdate = '%s', status = '%s',"
                " expectduration = '%d', price = '%d', ordertype = '%s',"
                " managerid = '%d'"
                " WHERE orderid = '%d'" % \
                (startdate, status, expectduration, price, ordertype, managerid, id)
            )
            db.commit()
            return redirect(url_for('order_detail.index', order=order, photographers=photographers, \
            aftereffects = aftereffects, id = id))

    return render_template('order_detail/detail_update.html', order=order, photographers=photographers, \
            aftereffects = aftereffects)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_order(id)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM porder WHERE orderid = '%d'" % (id,))
    db.commit()
    return redirect(url_for('dashboard.index'))