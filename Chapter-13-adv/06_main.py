from functools import reduce
sum = lambda a,b: a+b

l = [2,43,44,5,6,5,6]

val = reduce(sum, l)
print(val)