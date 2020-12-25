#!/usr/bin/env python3

import logging
import os
import sys
import colorlog

class Logger:
    log = None

    def __init__(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        date_format = '%d-%m-%Y %I:%M:%S %p'
        format = '%(asctime)s - %(levelname)-8s - %(message)s'

        if 'colorlog' in sys.modules and os.isatty(2):
            cformat = '%(log_color)s' + format
            f = colorlog.ColoredFormatter(cformat,
                                          date_format,
                                          log_colors={'DEBUG': 'cyan',
                                                      'INFO': 'white',
                                                      'WARNING': 'bold_yellow',
                                                      'ERROR': 'bold_red',
                                                      'CRITICAL': 'bold_red'
                                                      })
        else:
            f = logging.Formatter(format, date_format)
        ch = logging.StreamHandler()
        ch.setFormatter(f)
        root.addHandler(ch)
        self.log = logging.getLogger(__name__)



    def LogSyncronizer(self, level, mess):
        {
            "INFO": self.log.info,
            "DEBUG": self.log.debug,
            "WARN": self.log.warning,
            "CRITIC": self.log.critical,
            "ERROR": self.log.error
        }.get(level)(mess)















