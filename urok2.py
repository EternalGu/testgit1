def adder(*args, **kwargs):
    result = 0
    for num in args:
        result += num
    for num in kwargs:
        result += num
    return result

print(adder(2,3,4))