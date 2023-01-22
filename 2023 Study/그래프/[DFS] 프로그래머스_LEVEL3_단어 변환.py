answer = int(1e9)

def isDifferentOnlyOne(a, b):
    diffCount = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffCount += 1

    return True if diffCount == 1 else False

def dfs(nowWord, targetWord, words, wordSet, step):
    global answer

    if nowWord == targetWord:
        answer = min(answer, step)
        return

    for eachWord in words:
        if isDifferentOnlyOne(nowWord, eachWord) and eachWord not in wordSet:
            wordSet.add(eachWord)
            dfs(eachWord, targetWord, words, wordSet, step + 1)
            wordSet.remove(eachWord)

def solution(begin, target, words):
    wordSet = set()
    for eachWord in words:
        if isDifferentOnlyOne(begin, eachWord) and eachWord not in wordSet:
            wordSet.add(eachWord)
            dfs(eachWord, target, words, wordSet, 1)
            wordSet.remove(eachWord)

    return 0 if answer == int(1e9) else answer



begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))