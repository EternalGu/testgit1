def adder(*args, **kwargs):
    result = 0
    for num in args:
        if type(num) == int or type(num) == float or type(num) == bool:
            result += num
        else:
            try:
                result += float(num)
                continue
            except (ValueError, TypeError):
                pass
    for num in kwargs:
        if type(num) == int or type(num) == float or type(num) == bool:
            result += num
        else:
            try:
                result += float(num)
                continue
            except (ValueError, TypeError):
                pass
    return result

print(adder(2,3,4))


def countr(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@counter
def hello():
    print("Hello World")


hello()
hello()
print(hello.count)