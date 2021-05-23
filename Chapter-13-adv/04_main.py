def greeter_than_5(num):
    if num > 5:
        return True
    else:
        return False
lis = [2,33,43,54,5,56,7,6,7,8,7]
print(list(filter(greeter_than_5,lis )))