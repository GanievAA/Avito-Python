import sys
from datetime import datetime
from typing import Callable

original_write = sys.stdout.write


def my_write(string_text: str):
    """Функция добавляет время вывода на экран"""
    original_write(f'[{str(datetime.now())[0:-7]}]: {string_text}' + '\n')


sys.stdout.write = my_write
my_write('1, 2, 3')
sys.stdout.write = original_write


def timed_output(function: Callable):
    """Декоратор, который показывает время вывода на экран"""
    change_write = original_write

    def wrapper(string_text):
        change_write(f'[{str(datetime.now())[0:-7]}]: ')
        result = function(string_text)
        return result
    return wrapper


#@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')
    return 42

decorated = timed_output(print_greeting)
print(decorated('Nikita'))

# result = print_greeting("Nikita")
# print(type(result))

def redirect_output(filepath):
    """Декоратор, которые записывает все выводы функции print в файл. Файл будет храниться в filepath """
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            sys.stdout = open(filepath, 'w')
            result = func(*args, **kwargs)
            return result
        return inner_wrapper
    return wrapper


@redirect_output(r'C:\Users\Abdurakhim\Desktop\function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


calculate()
