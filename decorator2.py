# Decorators
# Level 2
# More details in this level about decortors.

'''
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper function executed before {original_function.__name__}')
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorator_display = decorator_function(display)
decorator_display()
# >> wrapper function executed before display
# >> display function ran
'''

'''
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper function executed before {original_function.__name__}')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')
display()
# >> wrapper function executed before display
# >> display function ran
'''

'''
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper function executed before {original_function.__name__}')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran {name}, {age}')
display_info('Sobhan', 24)
# >> TypeError: wrapper_function() takes 0 positional arguments but 2 were given
'''

'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper function executed before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran {name}, {age}')
display_info('Sobhan', 24)
display()
# >>wrapper function executed before display_info
# >>display_info ran Sobhan, 24
# >>wrapper function executed before display
# >>display function ran
'''