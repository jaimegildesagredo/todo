# -*- coding: utf-8 -*-

from tornado import web

from todo import models


class IndexHandler(web.RequestHandler):
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



class TasksHandler(web.RequestHandler):
    def initialize(self, store):
        self.store = store

    def post(self, task_id):
        method = self.get_argument('_method', '')
        if method.lower() == 'put':
            self.put(task_id)

    def put(self, task_id):
        task = self.store.get(models.Task, task_id)
        task.done = self.get_argument('done', False)

        self.store.add(task)
        self.store.commit()

        self.redirect('/')
