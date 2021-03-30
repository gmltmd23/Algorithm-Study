import copy

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # URDL

size = tuple(map(int, input().split()))
x, y, dir = map(int, input().split())
game_map = []
count = 1
for i in range(size[0]):
    game_map.append(list(map(int, input().split())))
check_map = copy.deepcopy(game_map)
check_map[x][y] = 1

while True:
    move = False
    for i in range(4):
        dir = 3 if not dir else dir - 1
        nx, ny = (x + dx[dir]), (y + dy[dir])
        if 0 <= nx < size[0] and 0 <= ny < size[1]:
            if not check_map[nx][ny]:
                x, y = nx, ny
                check_map[x][y] = 1
                count += 1
                move = True
                break
    if not move:
        nx, ny = (x + dx[(dir + 2) % 4]), (y + dy[(dir + 2) % 4])
        if 0 <= nx < size[0] and 0 <= ny < size[1]:
            if not game_map[nx][ny]:
                x, y = nx, ny
            else:
                break
        else:
            break

print(count)