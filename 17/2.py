
matrix = []

with open("17/data") as file:
    for line in file:
        matrix.append([*map(int, line.strip())])

size = len(matrix)
visited = [[size ** 2 * 10] * size for _ in range(size)]
stack = [(0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 1, 0, 0, 0)]

def insert(item, a, b):
    pivot = (a + b) // 2
    if a == pivot:
        stack.insert(pivot + 1, item)
        return
    if item[2] > stack[pivot][2]:
        insert(item, pivot + 1, b)
    else:
        insert(item, a, pivot - 1)

def move(x, y, c, pxd, pyd, cxd, cyd, step, worse):
    nx, ny = x + cxd, y + cyd
    ns = step + 1 if (cxd == pxd and cyd == pyd) else 1
    if cyd == -pyd and cxd == -pxd:
        return
    if nx < 0 or nx >= size or ny < 0 or ny >= size:
        return
    if ns > 10:
        return
    mc = c + matrix[nx][ny]
    if mc < visited[nx][ny]:
        worse = 0
        visited[nx][ny] = mc
    elif worse + 1 > 10:
        return
    else:
        worse += 1
    insert((nx, ny, mc, cxd, cyd, ns, worse), 0, len(stack))

while stack:
    x, y, c, xd, yd, step, worse = stack.pop(0)
    if step < 4:
        move(x, y, c, xd, yd, xd, yd, step, worse)
    elif x + 1 == size and y + 1 == size:
        print(c)
        break
    else:
        move(x, y, c, xd, yd, 0, -1, step, worse)
        move(x, y, c, xd, yd, -1, 0, step, worse)
        move(x, y, c, xd, yd, 1, 0, step, worse)
        move(x, y, c, xd, yd, 0, 1, step, worse)
