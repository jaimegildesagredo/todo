# -*- coding: utf-8 -*-

import httplib

from tornado import web

from todo import models


class IndexHandler(web.RequestHandler):
    def initialize(self, store):
        self.store = store

    def get(self):
        self.render('index.html', tasks=self.store.find(models.Task))

    def post(self):
        self.store.add(models.Task(body=self.get_argument('body')))

        self.store.commit()

        self.set_status(httplib.CREATED)


class TaskHandler(web.RequestHandler):
    def initialize(self, store):
        self.store = store

    def post(self, task_id):
        method = self.get_argument('_method', '').lower()

        if method == 'put':
            self.put(task_id)
        elif method == 'delete':
            self.delete(task_id)
        else:
            raise web.HTTPError(httplib.METHOD_NOT_ALLOWED)

    def put(self, task_id):
        task = self.store.get(models.Task, task_id)
        task.done = self.get_argument('done', False)

        self.store.add(task)
        self.store.commit()

    def delete(self, task_id):
        task = self.store.get(models.Task, task_id)

        self.store.delete(task)
        self.store.commit()
