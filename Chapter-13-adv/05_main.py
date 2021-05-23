def greeter(num):
    if num > 5:
        return True
    else:
        return False
ls = [34,3,54,5,567,68778,8,9,4,3,332,21,2,23]
b = list(filter(greeter, ls))
print(b)