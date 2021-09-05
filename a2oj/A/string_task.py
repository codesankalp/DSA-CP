s = input()
v = ["a", "o", "y", "e", "u", "i"]
ns = ""
for i in s.lower():
    if i in v:
        continue
    else:
        ns += f".{i}"
print(ns)
