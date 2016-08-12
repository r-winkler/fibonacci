# fibonacci.py

import sys

""" print fibonacci numbers till to upper limit """
def fibonacci(n):
    i = 0;
    j = 1;
    print(i)
    while j <= n:
        print(j);
        tmp = j;
        j = i + j;
        i = tmp

""" recursive approach: give nth fibonacci number """
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)


def parseToInt(str):
    try:
        return int(str)
    except:
        print('Could not parse argument to int.')


def show_program_arguments(arguments):
    for arg in arguments:
        print(arg)


if __name__ == '__main__':
    print('-' * 80)
    show_program_arguments(sys.argv)
    print('-'*80)
    fibonacci(parseToInt(sys.argv[1]))