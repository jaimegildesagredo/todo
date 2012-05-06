# -*- coding: utf-8 -*-

from cormoran import *


class Task(Persistent):
    body = StringField()
    done = BooleanField()
