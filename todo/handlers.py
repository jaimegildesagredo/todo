# -*- coding: utf-8 -*-

from tornado import web

from todo import models


class TasksHandler(web.RequestHandler):
    def initialize(self, store):
        self.store = store

    def get(self):
        self.render('index.html', tasks=self.store.find(models.Task))

    def post(self):
        self.store.add(models.Task(
            body=self.get_argument('body'),
            done=False))

        self.store.commit()

        self.redirect('/')
