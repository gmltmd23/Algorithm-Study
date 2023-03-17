INF = int(1e9)
answer = INF

def isOnlyOne(nowWord, targetWord):
    count = 0
    for i in range(len(nowWord)):
        if nowWord[i] != targetWord[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False

def dfs(nowWord, targetWord, visited, words, step):
    global answer
    if nowWord == targetWord:
        answer = min(answer, step)
        return

    for candidateWord in words:
        if (candidateWord not in visited) and (isOnlyOne(nowWord, candidateWord)):
            visited.add(candidateWord)
            dfs(candidateWord, targetWord, visited, words, step + 1)
            visited.remove(candidateWord)

def solution(begin, target, words):
    visited = set()
    visited.add(begin)
    dfs(begin, target, visited, words, 0)

    return answer if answer < INF else 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))