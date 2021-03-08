def rectangularSquare(n: int, cost: list(), q: int, queries: list()):
    # Write your code here
    answers = []
    for query in queries:
        lsx = []
        lsy = []
        ans = 0
        x, y, l, b = query
        # for x1 in range(n):
        #     if abs(x-x1) <= l:
        #         # temp[x1] = [1]*n
        #         lsx.append(x1)
        # for y1 in range(n):
        #     if abs(y-y1) <= b:
        #         lsy.append(y1)
        # print(lsx, lsy)
        # for x1 in lsx:
        #     for y1 in lsy:
        #         if abs(x-x1) <= l and abs(y-y1) <= b:
        #             ans += cost[x1][y1]

        # for i in range(n*n):
        #     x1 = i//n
        #     y1 = i % n
        #     if abs(x-x1) <= l and abs(y-y1) <= b:
        #         ans += cost[x1][y1]
        p, q = x-l, x+l
        r, s = y-b, y+b
        print(p, q, r, s)
        print()
        for i in range(p, q+1):
            for j in range(r, s+1):
                ans += cost[i][j]

        # while p < q:
        #     while r < s:
        #         ans += cost[p][r]
        #         p += 1
        #         r += 1

        # for x1 in range(x-l, n):
        #     for y1 in range(y-b, n):
        #         # if abs(x-x1) <= l and abs(y-y1) <= b:
        #         print(x1, y1)
        #         ans += cost[x1][y1]
        # if x <= l and y <= b:
        #     for i in range()
        answers.append(ans)
        # print("\n")
    return answers


def main():
    n = int(input())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    q = int(input())
    queries = [map(int, input().split()) for _ in range(q)]
    answers = rectangularSquare(n, matrix, q, queries)
    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
