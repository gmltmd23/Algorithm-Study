"""

프로그래머스 위클리 3주차_퍼즐 조각 채우기

생각보다 까다로운 부분들이 있어서 난이도가 있던 문제였다.
코드도 꽤 길게나오고 몇 군데 이쁘게 만들려다보니깐 비효율적일수도 있는데
일단 정확성만 테스트 하는 문제이기 때문에 괜찮다.

일단 기본적으로 이 문제를 풀기 위해서는 아이디어가 3가지 필요하다.

1. 일단 행렬을 탐색해야되니 기본적으로 DFS 또는 BFS를 사용해야한다.
2. 도형을 회전 시킬 수 있어야 한다.
3. 근데 그 회전 시킨 도형들을 기준점을 정해서 모두 같은 기준으로 만들어 줘야한다.

여기서 가장 주목해야할 아이디어는 3번이다.
나같은 경우에는 도형들이 최대한 (0, 0)에서 스타트 하게끔 만들어줬다. (standardize 과정)
그렇게 한 뒤 도형이 A,B 이렇게 두가지가 존재한다면
[set(A를 회전시킨 모든 도형들), set(B를 회전시킨 모든 도형들)] 이렇게 리스트로 만들어줬다. (그 리스트의 이름이 rt)

이제 game_board에서 빈칸인 0을 찾아 dfs를 하고
나온 좌표들을 standardize하여 rt에서 찾아주는 방식을 하니깐 풀 수 있었다.


"""

def dfs(cmp, value, x, y, table, result):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < len(table) and 0 <= ny < len(table):
            if table[nx][ny] == cmp:
                table[nx][ny] = value
                result.append((nx, ny))
                dfs(cmp, value, nx, ny, table, result)

def rotate(shapes, n):
    result = []

    for i in range(len(shapes)):
        result.append([shapes[i]])
        for _ in range(3):
            temp = []
            for x, y in result[-1][-1]:
                temp.append((y, n - 1 - x))
            result[-1].append(standardize(sorted(temp)))
        result[-1][0] = standardize(sorted(result[-1][0]))

    return result

def standardize(shape):
    new_shape = []
    s_x, s_y = shape[0][0], shape[0][1]
    for pos in shape:
        x, y = pos
        new_shape.append((x - s_x, y - s_y))
    return tuple(new_shape)

def make_set(rt):
    for i in range(len(rt)):
        rt[i] = set(rt[i])

def solution(game_board, table):
    answer, shapes = 0, []
    for x in range(len(table)):
        for y in range(len(table)):
            if table[x][y] == 1:
                table[x][y], temp = 0, [(x, y)]
                dfs(1, 0, x, y, table, temp)
                shapes.append(sorted(temp))
    rt = rotate(shapes, len(table))
    make_set(rt)

    for x in range(len(game_board)):
        for y in range(len(game_board)):
            if game_board[x][y] == 0:
                game_board[x][y], temp = 1, [(x, y)]
                dfs(0, 1, x, y, game_board, temp)
                tt = tuple(standardize(sorted(temp)))
                for i in range(len(rt)):
                    if tt in rt[i]:
                        answer += len(temp)
                        rt.pop(i)
                        break

    return answer