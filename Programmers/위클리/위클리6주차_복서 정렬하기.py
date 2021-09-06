"""

프로그래머스 위클리 6주차_복서 정렬하기

구현 + 정렬 문제이다.
구현같은 경우에는 조건에 잘 맞춰서 구현만 해주면 되는거고..
파이썬에서 정렬은 sort 또는 sorted의 key를 잘 활용하기만 쉽게 끝낼수가 있다.
어려운 문제는 아니지만 이런식의 문제가 코테에 거의 매번 나오기때문에 반드시 계속 연습해줘야한다.

"""

def get_winning_results(weights, h2h):
    winning_rates, heavy_winning = [0] * len(h2h), [0] * len(h2h)
    for i in range(len(h2h)):
        total, win = 0, 0
        for j in range(len(h2h)):
            if h2h[i][j] != 'N':
                total += 1
            if h2h[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    heavy_winning[i] += 1
        if total != 0:
            winning_rates[i] = (win / total) * 100
    return winning_rates, heavy_winning

def solution(weights, head2head):
    answer = []
    wr, hw = get_winning_results(weights, head2head)

    boxers = []
    for i in range(len(weights)):
        boxers.append([wr[i], hw[i], weights[i], (i + 1)])
    boxers.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    for boxer in boxers:
        answer.append(boxer[-1])

    return answer