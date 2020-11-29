n1 = input()
n2 = input()
for i in range(len(n1)):
    if abs(int(n1[i]) - int(n2[i])) == 1:
        print(1,end="")
    else:
        print(0,end="")
