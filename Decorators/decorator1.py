# Decorators
# Level 1
# Before becoming an expert in decorator, it is better to review these simple codes.
'''
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()

outer_function()
>>> Hi
'''
'''
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()
my_func()
my_func()
my_func()
>>> Hi
>>> Hi
>>> Hi
'''

def outer_function(msg):
    # message = msg

    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function(msg='Hi')
bye_func = outer_function(msg='Bye')
hi_func()
bye_func()
# >> Hi
# >> Bye


