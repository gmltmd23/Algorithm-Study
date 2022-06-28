"""

백준 문제 10775번 공항

우선 비행기는 i 순서로 들어온다고 하니깐, 정렬로 접근을 하면 안된다.

처음에 풀었던 코드는 아마 정확도 테스트는 다 통과할거다, 그렇게 만들어놨으니
그런데 시간복잡도가 O(n^2)가 나오는 코드라서 그런지 시간초과가 발생한다.

그말인즉슨 시간복잡도를 아마 O(n) 또는 적어도 O(n*log n) 까지는 만들라는 뜻일거다.
비행기를 게이트에 할당하는 과정에서 시간을 줄여야된다.

그런데 그 방법이 생각이 나지않아서, 인터넷을 참조하니 Union - Find를 사용하면
시간을 단축할수 있다고 한다. union-find를 써서 남아있는 게이트 수를 줄여가는 방법이다.

창의적인 방법이다. 꼭 복습해서 익히자.

"""

"""

이게 처음에 풀었던 코드

import sys
input = sys.stdin.readline

g, p = int(input()), int(input())
count = 0
gates = [_ for _ in range(g + 1)]
flights = []
for _ in range(p):
    flights.append(int(input()))

for airplane in flights:
    if gates[airplane] == 0:
        break
    count += 1
    gates[airplane] -= 1
    for i in range(airplane + 1, g + 1):
        gates[i] -= 1
print(count)

"""

import sys
input = sys.stdin.readline

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

g, p = int(input()), int(input())
count = 0
parents = [_ for _ in range(g + 1)]
planes = []
for _ in range(p):
    planes.append(int(input()))

for plane in planes:
    x = find_parent(parents, plane)
    if x == 0:
        break
    union(parents, x, x - 1)
    count += 1
print(count)