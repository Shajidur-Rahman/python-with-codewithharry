sub1 = int(input('enter marks: '))
sub2 = int(input('enter marks: '))
sub3 = int(input('enter marks: '))
plus = (sub1+sub2+ sub3)
result = (plus*100)/300
if sub1<33 or sub2<33 or sub3<33:
    print('The student is failed')
elif result < 40:
    print('The student is failed')
else:
    print('The student is passed')