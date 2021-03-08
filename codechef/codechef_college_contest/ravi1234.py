n = int(input())
bomb = input().replace(' ', '')
ans = max(len(max(bomb.split('1'))), len(max(bomb.split('0'))))
print(ans)
