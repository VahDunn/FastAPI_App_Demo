import logging.config
import uvicorn
import os



script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, 'logs', 'log.txt')
logging.FileHandler(log_path)

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'api.log',
            'maxBytes': 1024*1024,
            'backupCount': 5,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(logging_config)
LOG = logging.getLogger(__name__)

LOG.info("API is starting up")
LOG.info(uvicorn.Config.asgi_version)