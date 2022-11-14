import os


def get_current_env():
    return os.environ.get('ENVIRONMENT', 'LOCAL')


def is_local():
    return get_current_env() == 'LOCAL'
