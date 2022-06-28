"""

(복습) 프로그래머스 해시_위장 : LEVEL2

계산을 해주는 방법은 우선 category에 저장된 모든 수를 곱해주면
옷을 섞어서입는 모든 경우의 수가 나온다.

근데 그냥 곱하지않고
result *= (count + 1) 이렇게 count에 +1을 해주는 이유는
자기 자신을 뺴고 다른 카테고리끼리 섞어 입었을 경우를 계산해주기 위해서임
그리고 마지막에 또 return할때 result - 1을 하는데 -1을 하는 이유는
몸에 최소한 한가지는 걸쳐야 하기때문에 다 벗은경우를 빼줘야되서 -1을 한다.

"""

def solution(clothes):
    closet = {}
    for cloth, category in clothes:
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1

    result = 1
    for count in closet.values():
        result *= (count + 1)
    return result - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))