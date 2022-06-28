"""

프로그래머스 DP_등굣길 : LEVEL 3

다른 DP문제보다는 난이도가 있었던 문제
우선 puddles을 set으로 만들어줘서 시간복잡도를 낮춰주고,
dp식을 만들어본다.

움직일수 있는 방식은 오른쪽 또는 아래쪽
결국 table[x][y]에 도달하는 방법은 table[x][y-1] 에서 오거나 table[x-1][y]에서 오는것뿐이다.
그러면 식은 이렇게 나온다.

DP식 : table[x][y] = table[x - 1][y] + table[x][y - 1]
이 뜻은 [x, y]에 도달하는 방법의 가지수는 ( [x - 1][y]까지 필요한 방법의 수 + [x][y - 1]까지 필요한 방법의 수 ) 가 되는것이다.

x == 1 or y == 1 일때 다 1로 만드는 이유는 어차피 벽에 붙어있기때문에 위에서 내려오거나, 왼쪽에서 올수가 없는 즉 한가지 경우밖에 없게되기 때문에 그렇다.
그러니깐 [1,3]에 도달하려면 반드시 [1, 1] -> [1, 2] -> [1, 3] 이렇게 거쳐서 오는 1가지 방법밖에 없기때문에 싹다 1로 만들어주고

나머지 puddles에 해당하지 않는 좌표들에만 위의 DP식으로 쫙 뽑아내주면 된다.

복습하자

"""

def solution(m, n, puddles):
    table, pud = [[0] * (m + 1) for _ in range(n + 1)], set()
    for i, j in puddles:
        pud.add((i, j))

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (y, x) in pud:
                table[x][y] = 0
            elif x == 1 and y == 1:
                table[x][y] = 1
            else:
                table[x][y] = table[x - 1][y] + table[x][y - 1]

    return table[n][m] % 1000000007