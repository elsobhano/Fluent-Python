# Decorators
# Level 3
# Implementing decorators with classes.
# Maybe some python learners find classes easier than functions
# for the rest of the toturial we will continue with functions.

class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f'call method executed before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name, age):
    print(f'display_info ran {name}, {age}')

display_info('Sobhan', 24)
display()