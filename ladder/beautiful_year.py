y = int(input())+1
a,b,c,d = str(y)
while True:
    a,b,c,d = str(y)
#     print(a,b,c,d)
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        break
    y+=1
print(y)
