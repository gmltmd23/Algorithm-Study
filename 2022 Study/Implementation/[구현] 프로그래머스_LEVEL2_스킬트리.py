def solution(skill, skill_trees):
    upperAlphabet = [-1] * 26
    skillSet = set()
    for order, element in enumerate(skill):
        upperAlphabet[ord(element) %  ord('A')] = order
        skillSet.add(element)

    answer = len(skill_trees)
    for nowSkill in skill_trees:
        order = 0
        for element in nowSkill:
            if element in skillSet:
                if upperAlphabet[ord(element) % ord('A')] == order:
                    order += 1
                else:
                    answer -= 1
                    break

    return answer



skill = 'CBD'
skillTrees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skillTrees))