data = input()
x, y = int(data[1]), (ord(data[0]) - 96)
dx, dy = [0, 0, -2, 2], [-2, 2, 0, 0] #LRUD
dn = [-1, 1]
count = 0

for i in range(4):
    for j in range(2):
        nx, ny = (x + dx[i]), (y + dy[i])
        if i <= 1:
            nx += dn[j]
        else:
            ny += dn[j]
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            count += 1

print(count)

"""
dx, dy, dn 이렇게 따로 정의해서 풀어도되지만
steps = [
    (-2, -1 ), (-1, -2), (1, -2), (2, -1 ),
    (2, 1), (1, 2), (-1, 2), (-2, 1) 
]

이렇게 한번에 정의해서 8번 반복시켜도 되는 문제
그러면 반복문은 이렇게 나왔을것이다.

for i in range(8):
    nx, ny = (x + steps[i][0]), (y + steps[i][1])
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

"""