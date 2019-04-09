import pymysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

def parse_sql(filename):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost',
                               user='photodev',
                               port=3306,
                               password='123456',
                               db='photo',
                               charset='utf8mb4',
                               conv=pymysql.converters.conversions,
                               cursorclass=pymysql.cursors.DictCursor)

           
        # g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    cursor = db.cursor()
    stmts = parse_sql('/Users/yehaolin/Downloads/test4/photo/schema_order.sql')
    for stmt in stmts:
        cursor.execute(stmt)
    
    db.commit()

#     for line in open('/Users/lanyifan/workspace/flask_work/test2/photo/schema.sql'):
        # cursor.execute(line)
#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
