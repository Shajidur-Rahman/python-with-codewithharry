print('Computer Turn: Snake(s) Water(w) or Gun(g)?')
ask = input('Your Turn: Snake(s) Water(w) or Gun(g)?')

import random
rand = random.randrange(0,3)
y = ''
if rand == 0:
    you = 's'
elif rand == 1:
    you = 'w'
else:
    you = 'g'
print(you)

if ask == you:
    print('The match id tie')
elif you == 'g' and ask == 'w':
    print('You won the match')
elif you == 's' and ask == 'g':
    print('You won the match')
elif you == 'w' and ask == 'g':
    print("Computer won the match")
elif ask == 's' and you == 'g':
    print("Computer won the match")
