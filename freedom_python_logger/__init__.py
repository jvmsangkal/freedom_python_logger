#!/usr/bin/env python
import sys
import logging
import configparser
import logging.handlers

from rainbow_logging_handler import RainbowLoggingHandler

LOGGING_LEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET
}


def logger(config_file):
    CONFIG = configparser.RawConfigParser()

    CONFIG.read(config_file)

    logger_config = CONFIG['logger']

    logger = logging.getLogger(logger_config['name'])

    logger.setLevel(LOGGING_LEVELS.get(logger_config['level'], logging.NOTSET))

    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s %(funcName)s():%(lineno)d\t%(message)s'
    )

    handler = RainbowLoggingHandler(
        sys.stderr,
        color_funcName=('black', 'yellow', True)
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    if CONFIG.has_section('file_logger'):
        file_logger_config = CONFIG['file_logger']

        fh = logging.handlers.RotatingFileHandler(
            file_logger_config['file_path'],
            maxBytes=int(file_logger_config['max_log_file_size']),
            backupCount=int(file_logger_config['backup_count'])
        )

        fh.setLevel(LOGGING_LEVELS.get(file_logger_config['level'],
                                       logging.NOTSET))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    if CONFIG.has_section('email_logger'):
        email_logger_config = CONFIG['email_logger']

        eh = logging.handlers.SMTPHandler(
            (email_logger_config['host'], email_logger_config['port']),
            email_logger_config['from'],
            email_logger_config['to'],
            email_logger_config['subject'],
            (email_logger_config['username'], email_logger_config['password']),
            ()
        )

        eh.setLevel(LOGGING_LEVELS.get(email_logger_config['level'],
                                       logging.NOTSET))
        eh.setFormatter(formatter)
        logger.addHandler(eh)

    return logger
