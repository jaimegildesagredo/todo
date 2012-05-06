# -*- coding: utf-8 -*-

import os.path

from tornado import web
from cormoran import *

from todo import handlers


def application(debug=False):
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        debug=debug,
        autoreload=debug
    )

    return web.Application([
        (r'/', handlers.TasksHandler)
    ], **settings)
