# (°C * 1.8) + 32 = °F
def convert(cel):
    result = (cel * 1.8) + 32
    return result
a = convert(18)
print(a)