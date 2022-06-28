"""

프로그래머스 스택/큐_주식가격 : LEVEL 2

DP로 풀수있을까 싶어서 고민을 좀 해봤는데, DP로는 안된다.
결국에는 요소 한가지씩 다 봐줘야 하기때문에..

이중 루프를 돌면서
다만 각 요소에 대한 값들을 계산해줄때 해당 결과를
스택처럼 push 해주면 된다.

break를 걸어서 속도를 높여주는건 덤이다.

"""

def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices) - (i + 1))
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[-1] -= (len(prices) - j - 1)
                break
    return answer

p = [1,2,3,2,3]
print(solution(p))