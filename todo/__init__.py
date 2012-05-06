# -*- coding: utf-8 -*-

import os.path

from tornado import web
from cormoran import *

from todo import handlers

def create_database(sqlite):
    if not sqlite._connection.execute('PRAGMA table_info("Task")').fetchall():
        sqlite._connection.execute('CREATE TABLE Task (_id INTEGER PRIMARY KEY, body TEXT, done BOOL)')


def application(debug=False):
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        debug=debug,
        autoreload=debug
    )

    sqlite = connect('sqlite:///tasks.sqlite')
    create_database(sqlite)

    store = Store(sqlite)

    return web.Application([
        (r'/', handlers.TasksHandler, dict(store=store))
    ], **settings)
