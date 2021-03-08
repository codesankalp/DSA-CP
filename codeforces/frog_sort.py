def base(n, w, l):
	if n==2:
		if w[0] == 1:
			return 0
		else:
			if l[0] == 1:
				return 2
			else:
				return 1

t = int(input())
for _ in range(t):
	n = int(input())
	w = list(map(int, input().split()))
	l = list(map(int, input().split()))
	if n==2:
		if w[0] == 1:
			print(0)
		else:
			if l[0] == 1:
				print(2)
			else:
				print(1)

	ans = 0
	if n==3:
		if w[0] == 1:
			if w[1] == 2:
				print(0)
			else:
				if l[1] == 1:
					print(2)
				else:
					print(1)
		elif w[0] == 2:
			if w[1] == 1:
				if l[0] == 1:
					print(3)
				elif l[0] == 2:
					print(2)
				else:
					print(2)
			else:
				if l[0] == 3:
					print(1)
				
		else:
			if w[1] == 1:
				pass
			else:
				pass