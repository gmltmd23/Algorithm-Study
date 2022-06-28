"""

백준 문제 19941 그리디_햄버거 분배

가벼운 그리디 문제였다. 따지고보면 거의 브루트포스 문제임
C++로도 다시 풀어봐야겠다.

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().rstrip())
answer = 0
for i in range(len(table)):
    if table[i] == 'P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and table[j] == 'H':
                answer += 1
                table[j] = 'X'
                break
print(answer)