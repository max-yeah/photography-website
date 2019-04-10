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
    if position.lower() == 'project manager':
        sql = ("SELECT * FROM projectmanager WHERE id = '%d'" % (id,))
    else:
        sql = ("SELECT * FROM photographer WHERE id = '%d'" % (id,))  
    cursor.execute(sql)

    profiles = cursor.fetchone()
    print(profiles)
    return render_template('profile/profile_index.html', profiles=profiles)

def get_profile(id, position, check_author=True):
    db = get_db()
    cursor = db.cursor()
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
    g.current = "profile"
    get_profile(id)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM post WHERE id = '%d'" % (id,))
    db.commit()
    return redirect(url_for('blog.index'))