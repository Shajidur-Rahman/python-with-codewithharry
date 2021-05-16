with open('donkey.txt') as r1:
    text = r1.read()
with open('copy.txt', 'w') as w:
    wri = w.write(text)