import logging

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
        },
    },

    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'app.log',
        },
    },

    'loggers': {
        'app': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
    },
}