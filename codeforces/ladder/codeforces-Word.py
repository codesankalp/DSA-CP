s = input()
lower = 0
upper = 0
for i in s:
    if i.islower():
        lower+=1
    else:
        upper+=1

if lower == upper:
    print(s.lower())
elif lower<upper:
    print(s.upper())
else:
    print(s.lower())
