import getpass
import bcrypt
import psycopg2.extras

from webstore.datastore.pgdb import conn, get_cursor
from webstore.logger import logging

logger = logging.getLogger(__name__)


def add_user(screen_name, email, group_name, pingapi_uid=None):
    group = get_group_by_name(group_name)
    group_id = group['group_id']
    cur = get_cursor()
    sql = ('INSERT INTO webstore.users '
           '(screen_name, email, group_id, pingapi_uid) '
           'values (%s, %s, %s, %s) '
           'RETURNING user_id')
    try:
        cur.execute(sql, (screen_name, email, group_id, pingapi_uid))
        conn.commit()
        user_id = cur.fetchone()[0]
        return user_id
    except Exception as ex:
        conn.rollback()
        raise ex


def get_user_by_screen_name(screen_name):
    sql = ('SELECT * FROM webstore.users '
           'WHERE screen_name = %s ')
    cur = get_cursor()
    cur.execute(sql, (screen_name,))
    user_row = cur.fetchone()
    return user_row


def get_user_by_id(user_id):
    sql = ('SELECT * FROM webstore.users '
           'WHERE user_id = %s ')
    cur = get_cursor()
    cur.execute(sql, (user_id,))
    user_row = cur.fetchone()
    return user_row
