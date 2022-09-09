def solution(gems):
    answer = [0, len(gems) - 1]

    dict = {gems[0] : 1}
    totalGemKinds = len(set(gems))
    left, right = 0, 0
    while left < len(gems) and right < len(gems):
        if len(dict) == totalGemKinds:
            if (right - left) < (answer[1] - answer[0]):
                answer[0], answer[1] = left, right
            if dict[gems[left]] == 1:
                del dict[gems[left]]
            else:
                dict[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right == len(gems):
                break
            if gems[right] not in dict:
                dict[gems[right]] = 0
            dict[gems[right]] += 1

    return [answer[0] + 1, answer[1] + 1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))