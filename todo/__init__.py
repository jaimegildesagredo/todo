# -*- coding: utf-8 -*-

import os.path

from tornado import web
from cormoran import connect

from todo import handlers

def create_sqlite_table(conn):
    if not conn._connection.execute('PRAGMA table_info("Task")').fetchall():
        conn._connection.execute('CREATE TABLE Task (_id INTEGER PRIMARY KEY, body TEXT, done BOOL)')


def application(debug=False):
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        debug=debug,
        autoreload=debug
    )

    connection = connect('sqlite:///tasks.sqlite')
    create_sqlite_table(connection)

    handler_init = {'connection': connection}

    return web.Application([
        (r'/', handlers.IndexHandler, handler_init),
        (r'/tasks/(\d+)', handlers.TaskHandler, handler_init)
    ], **settings)
