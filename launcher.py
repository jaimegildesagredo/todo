#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import tornado.options
import tornado.ioloop

from todo import application

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    tornado.options.enable_pretty_logging()

    try:
        application(debug=True).listen(8888)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
