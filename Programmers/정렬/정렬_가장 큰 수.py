"""

프로그래머스 정렬_가장 큰 수 : LEVEL 2

이거 레벨2 인데 꽤 어려운 문제이다.
초반에는 permutations 문제인줄 알고 풀었더니 시간초과로 안풀렸음..

코드는 짧게 나오는데 이게 사전적 정렬을 모르면 풀수가 없는 문제이다.

숫자로 정렬을 하지않고, str 상태로 3을 곱해 사전적인 순서로 정렬을 시켜줘야만 풀수있는 문제이다.
아무리 생각해도 방법이 떠오르지 않아 인터넷을 참조한 문제이다.

꼭 복습을 해야하는 문제이다. 나중에 써먹을수 있는 테크닉같다.

"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))