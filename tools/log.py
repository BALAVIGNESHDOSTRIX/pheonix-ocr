# -*- coding: utf-8 -*-
from config import config
conf = config.log or {}
import logging
from logging.handlers import RotatingFileHandler

active = conf.get('active')
def getLogHandler(app):
    if active:
        maxBytes = conf.get('maxBytes', 1024 * 1024 * 5)
        backupCount = conf.get('backupCount', 5)
        logfile = conf.get('logfile')
        if logfile:
            if conf.get('logrotate'):
                handler = RotatingFileHandler(logfile, maxBytes=maxBytes, backupCount=backupCount)
            else:
                handler = logging.FileHandler(logfile)
            handler.setLevel(logging.INFO)
            log_format = conf.get('log_format')
            if log_format:
                log_format = logging.Formatter(log_format)
                handler.setFormatter(log_format)
            return handler
        app.logger.error("Log Configuration (logfile) key missing ...!!!")
        return
    app.logger.error("Please Activate Log Configuration...!")
    return