def game():
    return 123
with open('game.txt') as r:
    highscore = int(r.read())
gamescore = game()
if highscore < gamescore:
    with open('game.txt', 'w') as w:
        w.write(str(gamescore))