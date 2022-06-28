"""

백준 문제 2812번 크게 만들기

문제 설명이 겁나 짧은 그리디 문제지만, 난이도는 굉장히 높은 문제이다.
스택구조를 사용하지않으면 절대 풀수가 없는 문제.

아무리 고민해봐도 풀이방법이 떠오르지않아서, 다른사람들이 풀은것을 참고하였다.
스택을 이용해서 큰값을 걸러내는 방법이 예술이다 아주.

마지막 출력할때 stack[:n - k]로 슬라이싱을 해서 쓰는데, 스택에 쓸모없는 추가적인 값이 들어갈때가 있어서 그런것 같다.

꼭 복습을 하자.

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = list(input().rstrip())
count, stack = k, []

for i in range(n):
    while count > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        count -= 1
    stack.append(number[i])
print(n-k)
print(stack)
print("".join(stack[:n - k]))