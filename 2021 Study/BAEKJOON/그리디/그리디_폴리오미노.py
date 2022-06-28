"""

백준 문제 1343번 그리디_폴리오미노

그리디 문제이면서 구현 문제이다.
이런 문제들이 코딩테스트에서 의외로 자주 나온다.

난이도가 높은 문제가 아니기 때문에, 설명을 천천히 읽으면서 풀면 다 풀린다.
시간이 여유로우면 코드를 더 이쁘게 리팩토링 해보는것도 좋을 것 같다.

"""

import sys
input = sys.stdin.readline

def make_answer(answer, count):
    if count >= 4:
        if ((count % 4) % 2) == 0:
            AAAA = count // 4
            BB = (count % 4) // 2
            answer += ('AAAA' * AAAA) + ('BB' * BB)
        else:
            return -1
    else:
        if count == 2:
            answer += 'BB'
        else:
            return -1
    return answer

def solution(count, board):
    answer = ""
    for i in range(len(board)):
        if board[i] == 'X':
            count += 1
        else:
            if count > 0:
                answer = make_answer(answer, count)
            if answer == -1:
                break
            else:
                answer += '.'
            count = 0

    return answer if count == 0 else make_answer(answer, count)

count, board = 0, input().rstrip()
print(solution(count, board))