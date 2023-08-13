# Decorators
# Level 4
# Here we will see some practical examples.

''''
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
 

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time
# @my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran {name}, {age}')

display_info('Saman', 18)
#>> display_info ran Saman, 18
#>> display_info ran in: 1.0005886554718018 sec
'''
'''
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
 

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper
'''
import time

'''
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran {name}, {age}')

display_info('Saman',18)
# display_info = my_timer(display_info)
# print(display_info.__name__) #>> wrapper
#>> display_info ran Saman, 18
#>> display_info ran in: 1.000819206237793 sec
## In this code we do not have any outputs from my_logger 
## This code create a new logger file -> wrapper.log
'''
'''
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran {name}, {age}')

display_info('Saman',18)
# >> display_info ran Saman, 18
# >> wrapper ran in: 1.002483606338501 sec
# ODD Output
'''
## Final Solution for all the challeges mentioned above
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
 
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran {name}, {age}')

display_info('Tom', 18)
