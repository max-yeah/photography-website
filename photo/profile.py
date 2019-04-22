from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from photo.auth import login_required
from photo.db import get_db

bp = Blueprint('profile', __name__)
# @bp.route('/profile/index', methods=('GET', 'POST'))

@bp.route('/<int:id>/<string:position>/profile/index', methods=('GET', 'POST'))
@login_required
def index(id, position):
    g.current = "profile"
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT phone FROM %s_phone WHERE id = '%d'" % (position, id,))
    phone = cursor.fetchone()
    if phone == None:
        cursor.execute("SELECT pos.id, pos.position position, pos.username username, pos.level level, "
        "pos.birthday birthday, pos.salary salary"
        " FROM %s pos"
        " WHERE pos.id = '%d'" % (position, id,))
        profiles = cursor.fetchone()
        profiles['phone'] = None
    else:
        cursor.execute("SELECT pos.id, pos.position position, pos.username username, pos.level level, "
                "pos.birthday birthday, pos.salary salary, MAX(phone.phone) phone"
                " FROM %s pos, %s_phone phone"
                " WHERE pos.id = '%d' AND"
                " pos.id = phone.id" % (position, position, id,))
        profiles = cursor.fetchone()
    if profiles['position'] == 'aftereffect':
        profiles['position'] = 'After Effect'
    if profiles['position'] == 'devicemanager':
        profiles['position'] = 'Device Manager'
    if profiles['position'] == 'projectmanager':
        profiles['position'] = 'Project Manager'
    if profiles['position'] == 'photographer':
        profiles['position'] = 'Photographer'
    return render_template('profile/profile_index.html', profiles=profiles)

def get_profile(id, position, check_author=True):   
    db = get_db()
    cursor = db.cursor()
    # position = "".join(position.split()) ## remove space
    sql = ("SELECT * FROM %s WHERE id = '%d'" % (position, id,))
    cursor.execute(sql)
    profiles = cursor.fetchone()

    if profiles is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and profiles['id'] != g.user['id']:
        abort(403)

    return profiles

@bp.route('/<int:id>/<string:position>/profile/update', methods=('GET', 'POST'))
@login_required
def update(id, position):
    g.current = "profile"
    profiles = get_profile(id, position)
    print(profiles)

    if request.method == 'POST':
        username = request.form['username']
        position = request.form['position']
        error = None


        if not username:
            error = 'Username is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()

            cursor.execute(
                "UPDATE %s SET username = '%s', position = '%s'"
                " WHERE id = '%d'" % \
                (position, username, position, id)
            )

            db.commit()
            return redirect(url_for('profile.index', id = id, position = position))
    return render_template('profile/profile_update.html', profiles=profiles)

@bp.route('/<int:id>/profile/delete', methods=('POST',))
@login_required
def delete(id):
    position = 'photographer' # just in case
    g.current = "profile"
    get_profile(id, position)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM post WHERE id = '%d'" % (id,))
    db.commit()
    return redirect(url_for('dashboard.index'))