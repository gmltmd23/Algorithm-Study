def solution(s):
    splitedString = s.split('},')

    numbers = []
    for element in splitedString:
        temp = []
        nowInteger = ''
        for c in element:
            if c.isdigit():
                nowInteger += c
            if c == ',':
                temp.append(int(nowInteger))
                nowInteger = ''
        if nowInteger != '':
            temp.append(int(nowInteger))

        numbers.append(temp)

    numbers.sort(key=lambda x: len(x))

    answer = []
    beforeSet = set()
    for i in range(len(numbers)):
        numbers[i] = set(numbers[i])
        temp = numbers[i] - beforeSet
        answer.append(temp.pop())
        beforeSet = numbers[i]

    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))