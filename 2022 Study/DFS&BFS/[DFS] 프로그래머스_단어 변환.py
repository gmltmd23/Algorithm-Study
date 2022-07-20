from collections import deque

def isDiffOnlyOne(begin, target):
    correctCount = 0
    for a, b in zip(begin, target):
        if a == b:
            correctCount += 1

    if correctCount == (len(begin) - 1):
        return True
    else:
        return False

def dfs(nowWord, target, wordsSet, count, everyResult):
    if nowWord == target:
        everyResult.append(count)
        return

    wordsList = list(wordsSet)
    for candidateWord in wordsList:
        if isDiffOnlyOne(nowWord, candidateWord):
            nextWordsSet = wordsSet.copy()
            nextWordsSet.remove(candidateWord)
            dfs(candidateWord, target, nextWordsSet, count + 1, everyResult)

def solution(begin, target, words):
    wordsSet = set(words)
    if target not in set(wordsSet):
        return 0

    everyResult = []
    dfs(begin, target, wordsSet, 0, everyResult)

    return min(everyResult)