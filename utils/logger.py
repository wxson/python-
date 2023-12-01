import logging

import colorlog


def init_logger():
    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)
    if not _logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        # fmt_string = '%(log_color)s[%(asctime)s][%(name)s][%(levelname)s]%(message)s'
        fmt_string = '%(log_color)s%(message)s'
        # black red green yellow blue purple cyan and white
        log_colors = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'purple'
        }
        fmt = colorlog.ColoredFormatter(fmt_string, log_colors=log_colors)
        stream_handler.setFormatter(fmt)
        _logger.addHandler(stream_handler)
    return _logger
