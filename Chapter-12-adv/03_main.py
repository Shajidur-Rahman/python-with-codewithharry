num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

try:
    res = num1/num2
    print(res)
except:
    print('dont input 0')
