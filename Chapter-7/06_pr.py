#num 1 problem


# num 2 problem
# li = ['harry', 'sohan', 'sochin', 'rahul']
# for i in li:
#     print(i)


# num 3 problem


# num 4 problem
num = int(input('Give me a number: '))
if num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0:
    if num in [2,3,5,7]:
        print('The number is a prime number')
else:
    print('The number is not a prime number')