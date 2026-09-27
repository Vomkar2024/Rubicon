
str = 'softwareengineering986884991'      
alph = []
num = []
for i in str:
    if i.isalpha():
        alph.append(i)
    else:
        num.append(i)
op = ''.join(sorted(alph)+sorted(num))
print(op)

