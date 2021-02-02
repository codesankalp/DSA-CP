def countPaths(maze, R, C):
    if (maze[0][0] == -1):
        return 0

    for i in range(R):
        if (maze[i][0] == 0):
            maze[i][0] = 1

        else:
            break

    for i in range(1, C, 1):
        if (maze[0][i] == 0):
            maze[0][i] = 1

        else:
            break

    for i in range(1, R, 1):
        for j in range(1, C, 1):

            if (maze[i][j] == -1):
                continue

            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i - 1][j])

            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i][j - 1])
    if (maze[R - 1][C - 1] > 0):
        return maze[R - 1][C - 1]
    else:
        return 0


def herculesMaze(n, m, maze):
    mat = []
    count = 0
    for i in maze:
        ls = []
        for j in i:
            if j == '.':
                ls.append(0)
            else:
                ls.append(-1)
                count += 1
        mat.append(ls)
    # print(mat)
    ans = countPaths(mat, n, m)
    return ans*count


def main():
    n, m = map(int, input().split())
    maze = []
    for row in range(n):
        maze.append(input())
    ans = herculesMaze(n, m, maze)
    print(ans)


if __name__ == "__main__":
    main()
