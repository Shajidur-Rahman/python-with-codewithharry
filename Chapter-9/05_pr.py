with open('donkey.txt') as r:
    text = r.read()
text = text.replace('donkey', "######")
with open('donkey.txt', 'w') as w:
    w.write(text)