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