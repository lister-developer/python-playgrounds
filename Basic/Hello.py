from dataclasses import dataclass
import logging

print("Hello world")

@dataclass
class MyData:
    name: str
    age: int

data = MyData(
    name="lister",
    age=18
)

logging.warning(data)

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(10))

def fib(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n - 1, b, a + b);
 
# Driver Code
n = 9;
print("fib("+str(n)+") = "+str(fib(n)))



import time as tt

def func():
    num = 0
    for i in range(10):
        num += i

    return num


def main():
    return func() + func() + func() + func() + func() + func() + func()


t1 = tt.time()
main()
print("Time taken: {}".format(tt.time() - t1))
# 9.05990e-6


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return f'hello world {self.i}' 
    
my = MyClass()
print(my.i)
print(my.__doc__)
print(my.f())