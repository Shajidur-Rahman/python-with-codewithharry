import random
computer = random.randrange(0,10)
i = 0
while i < 6:
    ask = int(input('Enter your number: '))
    if ask > computer:
        print('Please give me a small number')
    elif ask < computer:
        print('Please give me a big number')
    else:
        print('You won')
        exit()
    i = i + 1
    # if i == 5:
    #     print('You lost')
    #     print()
    #     exit() 
print(f'The number was {computer}')