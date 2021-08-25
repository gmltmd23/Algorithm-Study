"""

프로그래머스 DFS&BFS_단어 변환 : LEVEL 3

문제에서 제한하는 조건을 보면, 단어의 길이는 3~10
그리고 words의 갯수는 3~50(중복 단어없음)
즉 범위가 그리 크지않다, dfs나 bfs 뭘 쓰든 풀수있다.

문제에서는 한번에 한개의 단어만 바꿀수있고, words에 있는 단어만 쓰라고한다.
이거를 그래프처럼 생각해보면 한번에 한개의 단어만 바꿀수있는것
즉 begin의 단어와 words의 단어들 중에 스펠링 차이가 한개만 나는것이
노드-노드 처럼 연결됬다고 생각하면 된다.

바꿀수 있는것들을 리스트에 넣고 그것들에 대하여 각각 방문확인set(리스트로 해도되지만 문자열 대조때문에, set이 더 효율적이라 set으로 했다.)을
생성해줘서 target 단어를 만들수있을때까지 쭈우우우욱 진행한다.

그럼 target 단어를 만들수있는 여러가지 경우의 수가 생기는데 그 중에서
count값이 제일 작은게 답이 된다.

나는 이거를 every라는 리스트를 만들고 그곳에 count 값을 모아 min을 했는데
min을 구하는 시간까지 걱정된다면 차라리 count를 전역변수 설정하고 최소값을 구해줘도 될거같다.

"""

def diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False

    if count == 1:
        return True
    else:
        return False

def dfs(begin, target, check, count, every):
    if begin == target:
        every.append(count)
        return

    temp, waited = list(check), []
    for i in range(len(temp)):
        if diff(begin, temp[i]):
            waited.append(temp[i])

    for w in waited:
        next_check = check.copy()
        next_check.remove(w)
        dfs(w, target, next_check, count + 1, every)
    return

def solution(begin, target, words):
    answer = 0
    check, every = set(words), []
    if target not in check:
        return answer

    dfs(begin, target, check, 0, every)
    return min(every)