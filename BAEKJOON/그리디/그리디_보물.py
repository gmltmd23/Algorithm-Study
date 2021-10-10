"""

백준 문제 1026번 그리디_보물

쉬운 문제였다.
그래서 다른 풀이가 있는지 요리조리 고민 해봤는데
우선순위큐를 쓰든 뭘 쓰든 간에 결국 순서를 맞춰야해서

시간복잡도가 O(n * log n) 보다 작아지기는 힘들다.
그래서 코드가 간단한 sort로 문제를 해결하였다.
자바로도 풀어보자.

"""

import sys
input = sys.stdin.readline

n = int(input())
a, b = sorted(list(map(int, input().split())), reverse=True), sorted(list(map(int, input().split())))

answer = 0
for i in range(n):
    answer += a[i] * b[i]

print(answer)