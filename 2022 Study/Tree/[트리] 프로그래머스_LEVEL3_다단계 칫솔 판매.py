def solution(enroll, referral, seller, amount):
    earnedMoney, parent = {}, {}
    for i in range(len(enroll)):
        earnedMoney[enroll[i]] = 0
        parent[enroll[i]] = referral[i]

    for i in range(len(seller)):
        nowPerson, nowMoney = seller[i], amount[i] * 100
        while nowPerson != "-":
            tenPercentMoney = nowMoney * 0.1
            if tenPercentMoney < 1:
                earnedMoney[nowPerson] += nowMoney
                break
            else:
                earnedMoney[nowPerson] += (nowMoney - int(tenPercentMoney))
                nowPerson = parent[nowPerson]
                nowMoney = int(tenPercentMoney)

    answer = []
    for person in enroll:
        answer.append(earnedMoney[person])

    return answer



enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))