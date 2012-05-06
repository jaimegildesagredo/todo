# -*- coding: utf-8 -*-

from tornado import web


class TasksHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')
