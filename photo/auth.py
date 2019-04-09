import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from photo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    g.current = "unlogin"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        position = request.form['position']
        position = str(position)
        db = get_db()
        error = None
        cursor = db.cursor()
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not position:
            error = 'position is required.'
        else:
            if position.lower() == 'projectmanager':
                cursor.execute(
                    "SELECT id FROM ProjectManager WHERE username = '%s'" % (username,))
            # elif position.lower() == 'photographer':
            else:
                cursor.execute(
                    "SELECT id FROM Photographer WHERE username = '%s'" % (username,))
            if cursor.fetchone() != None:
                error = 'User {} is already registered. Or you have the wrong position'.format(username)

        if error is None:
            if position.lower() == 'projectmanager':
                cursor.execute(
                "INSERT INTO projectmanager (username, password, position) VALUES ('%s', '%s', '%s')" % \
                (username, generate_password_hash(password),position))
            elif position.lower() == 'photographer':
                cursor.execute(
                "INSERT INTO photographer (username, password, position) VALUES ('%s', '%s', '%s')" % \
                (username, generate_password_hash(password),position))
                # (username, 'apple',position)
            db.commit()
            return redirect(url_for('auth.login'))


    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    g.current = "unlogin"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        position = request.form['position']
        position = str(position)
        db = get_db()
        error = None
        cursor = db.cursor()
        if position.lower() == 'projectmanager':
            cursor.execute(
                "SELECT * FROM projectmanager WHERE username = '%s'" % (username,)
            )
        # elif position.lower() == 'photographer':
        else:
            cursor.execute(
                "SELECT * FROM photographer WHERE username = '%s'" % (username,)
            )
        user = cursor.fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        # elif position != user['position']:
        #     error = 'Incorrect position.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['user_position'] = user['position'] # 有点坑，大小写
            # return redirect(url_for('index'))
            return redirect(url_for('index'))


        print("error!!!", error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    user_position = session.get('user_position')
    user_position = str(user_position)
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        cursor = db.cursor()
        if user_position.lower() == 'projectmanager':
            cursor.execute(
                "SELECT * FROM projectmanager WHERE id = '%d'" % (user_id,)
            )
            g.user = cursor.fetchone()
        elif user_position.lower() == 'photographer':
            cursor.execute(
                "SELECT * FROM photographer WHERE id = '%d'" % (user_id,)
            )
            g.user = cursor.fetchone()
        

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view