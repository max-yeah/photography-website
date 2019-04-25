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
        password2 = request.form['password2']
        position = request.form['position']
        position = str(position)
        db = get_db()
        error = None
        cursor = db.cursor()
        if not username:
            error = 'Username is required.'
        elif password != password2:
            error = 'Password is inconsistant.'
        elif not position:
            error = 'position is required.'
        else:
            position = position.lower()
            if position == 'project manager':
                position = 'projectmanager'
            if position == 'device manager':
                position = 'devicemanager'
            if position == 'after effect':
                position = 'aftereffect'      
            cursor.execute(
                "SELECT id FROM %s WHERE username = '%s'" % (position, username,))
            if cursor.fetchone() == None:
                error = 'User {} Does not exist. Or you enter the wrong position'.format(username)

        if error is None:                
            cursor.execute(
            "UPDATE %s SET password = '%s' WHERE username = '%s'" % \
            (position, generate_password_hash(password), username))
            db.commit()
            return redirect(url_for('auth.login'))

        print("resigter page error is: ", error)
        return render_template('auth/register.html', error = error)

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
        position = position.lower()
        if position == 'project manager':
            position = 'projectmanager'
        if position == 'device manager':
            position = 'devicemanager'
        if position == 'after effect':
            position = 'aftereffect'
        if position == 'boss':
            position = 'projectmanager'
        cursor.execute(
            "SELECT * FROM %s WHERE username = '%s'" % (position, username,)
        )
        user = cursor.fetchone()

        if user is None:
            error = 'Incorrect username.'
        else:
            if not check_password_hash(user['password'], password):
                error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['user_position'] = user['position']
            return redirect(url_for('index'))


        return render_template('auth/login.html',error = error)

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
        cursor.execute(
            "SELECT * FROM %s WHERE id = '%d'" % (user_position, user_id,)
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