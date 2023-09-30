def typeNumber():
    print("21")

typeNumber()


def simpleDecorator(function):
    print("decorator is working")
    def wrapper():
        print("Decorator doing something")
        function()
        print("decorator end")
    return wrapper


#@simpleDecorator
def sayHi():
    print("Hello")

sayHi()
sayHiAdvanced = simpleDecorator(sayHi)
sayHiAdvanced()

def simpleDecorator_v2(function):
    print("decorator_v2 is working")

    def wrapper(*args, **kwargs):
        print("We have got", args, kwargs)
        print("Start")
        result = function(*args, *kwargs)
        print("end")
        return result

    return wrapper()


@simpleDecorator_v2
def add(a, b):
    print(a+b)


import time


def timeCheker(function):
    def wrapper(*args, **kwargs):
        timestart = time.time()
        result = function(*args, **kwargs)
        print("Time working - ", {time.time() - timestart})
        return result
    return wrapper()

@timeCheker
def func():
    print("Test func")
    time.sleep(1)

func()


def powerM(function):
    def wrapper():
        result = function("With decorator power")
        return result

    return wrapper()

@powerM
def func():
    print("21")

func()

