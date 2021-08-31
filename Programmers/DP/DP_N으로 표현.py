"""

프로그래머스 DP_N으로 표현 : LEVEL 3

DP문제는 역시 어렵다.. 인터넷에서 다른사람이 푼것을 보며
개념을 이해한 다음에 풀게 되었다.

실은 사칙연산 경우의 수 모두 때려넣어야 할거라고는 생각했는데
그러면 시간이 너무많이 걸릴까봐 안했지만, 문제를 읽어보니 범위가 1~9이더라..
그래서 dp를 이용해 반복문을 따라 숫자를 만들다가 number와 동일한게 해당 set에 존재하면
리턴, 끝까지 다했는데  존재하지않으면 -1을 리턴해주면된다.

그리고 다 풀었는데, 테스트케이스가 한개 통과가 안되길래
    if N == number:
        return 1
이 코드를 넣었더니 해결됬다.

반드시 복습을 해야하는 문제이다.

"""

def solution(N, number):
    if N == number:
        return 1

    arr = [0] + [{int(str(N) * i)} for i in range(1, 9)]
    for i in range(2, 9):
        for j in range(1, i):
            for num1 in arr[j]:
                for num2 in arr[i - j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2:
                        arr[i].add(num1 // num2)
        if number in arr[i]:
            return i
    return -1

solution(5, 12)