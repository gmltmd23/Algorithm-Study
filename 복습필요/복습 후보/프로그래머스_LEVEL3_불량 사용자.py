from itertools import permutations

def check(user, ban):
    if len(user) != len(ban):
        return False

    for i in range(len(user)):
        if user[i] == ban[i] or ban[i] == '*':
            continue
        else:
            return False

    return True

def solution(user_id, banned_id):
    answer = []
    for perm in permutations(user_id, len(banned_id)):
        count = 0
        for user, ban in zip(perm, banned_id):
            if check(user, ban):
                count += 1

        if count == len(banned_id):
            tempSet = set(perm)
            if tempSet not in answer:
                answer.append(tempSet)

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))