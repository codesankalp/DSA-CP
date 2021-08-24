def generate(st, s):
    if len(s) == 0:
        return
 
    # If current string is not already present.
    if s not in st:
        st.add(s)
 
        # Traverse current string, one by one
        # remove every character and recur.
        for i in range(len(s)):
            t = list(s).copy()
            t.remove(s[i])
            t = ''.join(t)
            generate(st, t)
 
    return
for _ in range(int(input())):
    s = input()
    st = set()
    generate(st, s)
    # print(st)
    for i in st:
        if sorted(list(set(i))) == sorted(list(set(s))):
            print(i)
    print()
