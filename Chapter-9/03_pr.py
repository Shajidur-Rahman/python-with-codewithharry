f = open('poems.txt')
txt = f.read()
if 'twinkle' in txt:
    print('Yes')
else:
    print('No')
f.close()