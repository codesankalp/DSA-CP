n = input()
four = n.count('4')
sev = n.count('7')
if four+sev == 4 or four+sev == 7:
    print("YES")
else:
    print("NO")
