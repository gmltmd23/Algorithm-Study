"""

해커랭크 Climbing the Leaderboard : Medium

어려운 문제였다.
일단 문제에서 조건의 범위가 굉장히 넓기때문에 이진탐색을 사용하는줄 알았다.
그래서 만든게 아래의 주석되있는 코드이다.

def climbingLeaderboard(ranked, player):
    answer = []
    ranked = sorted(set(ranked), reverse=True)
    for p in player:
        start, end = 0, len(ranked) - 1
        rank, flag = 0, 0
        while start <= end:
            mid = (start + end) // 2
            if p > ranked[mid]:
                end = mid - 1
                rank, flag = mid, -1
            elif p < ranked[mid]:
                start = mid + 1
                rank, flag = mid, 1
            else:
                rank, flag = mid, 0
                break

        if flag == -1:
            if end != -1:
                ranked = ranked[:rank] + [p] + ranked[rank:]
                answer.append(1 + rank)
            else:
                ranked = [p] + ranked
                answer.append(1)
        elif flag == 1:
            ranked = ranked[:rank + 1] + [p] + ranked[rank + 1:]
            answer.append(1 + rank + 1)
        else:
            answer.append(rank + 1)
    return answer

근데 문제는 정확도 측면에서는 100% 정답인거같은데
테스트케이스 6, 7, 9에서 시간초과가 발생한다.

아마도 ranked 배열을 슬라이싱하며 새로운 element를 추가하는 과정에서 시간복잡도가 O(n^2)이 넘어가는것 같다.
그말은 즉 이진탐색말고 다른 방법으로 풀으라는 뜻이다.

도저히 고민해봐도 풀이가 보이지가 않길래, Implemetation을 참고하였다.
이 문제의 핵심은 ranked 배열은 내림차순 정렬, player 배열은 오름차순 정렬이라는 점에있다.
영어 문제이다보니깐 문제를 대충읽어서 저 중요한 조건을 못읽었다..
문제 제대로읽자 ㅠㅠ 조건을 알고보면 크게 어려운 문제가 아니었다.

아래의 코드가 정답 풀이이다.

"""

def climbingLeaderboard(ranked, player):
    answer, ranked = [], sorted(set(ranked), reverse=True)
    idx = len(ranked) - 1
    for score in player:
        while ranked[idx] <= score and idx >= 0:
            idx -= 1
        if idx < 0:
            answer.append(1)
            continue
        answer.append(idx + 2)

    return answer