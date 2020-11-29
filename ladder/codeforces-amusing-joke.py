g_name = list(input())
r_name = list(input())
m_name = list(input())
# print(sorted(m_name) , sorted(g_name) , sorted(r_name), sep="\n")
if sorted(m_name) == sorted(sorted(g_name) + sorted(r_name)):
    print("YES")
else:
    print("NO")
