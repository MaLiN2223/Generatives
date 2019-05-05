import logging
import os
import logging.config
import logging.handlers



class Logger:
    logger = None
    statistics_logger = None
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(message)s'
            },
            'pure': {
                'format': '%(message)s'
            }
        },
        'handlers': {
            'mainlogger': {
                'class': 'logging.FileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': os.path.join('logs', 'application.log'),
                'encoding': 'utf8'
            },
            'statistics': {
                'class': 'logging.FileHandler',
                'level': 'INFO',
                'formatter': 'pure',
                'filename': os.path.join('logs', 'statistics.log'),
                'encoding': 'utf8'
            }
        },
        'loggers': {
            '': {
                'handlers': ['mainlogger','statistics'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }

    def __init__(self, name='mainlogger'):
        self.logger = logging.getLogger(name)

    def log_model(self, model):
        model.summary(print_fn=self.logger.info)

    @staticmethod
    def get_logger():
        if Logger.logger is None:
            Logger.logger = Logger()
        return Logger.logger

    @staticmethod
    def get_statistics_logger():
        if Logger.statistics_logger is None:
            Logger.statistics_logger = Logger('statistics')
        return Logger.statistics_logger

    def info(self, message):
        self.logger.info(message)

logging.config.dictConfig(Logger.logging_config)
