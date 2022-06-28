def findRange(num):
    number = str(num)
    length = len(number)
    max_target = number[0] if int(number[0]) < 9 else ''
    max_result = number[0] if max_target == '' else '9'
    min_target = number[0] if int(number[0]) > 1 else ''
    min_result = number[0] if min_target == '' else '1'

    for i in range(1, length):
        if max_target != '':
            if number[i] == max_target:
                max_result += "9"
            else:
                max_result += number[i]
        else:
            if number[i] != '9' and number[i] != number[0]:
                max_target = number[i]
                max_result += '9'
            else:
                max_result += number[i]

        if min_target != '':
            if number[i] == min_target:
                if min_target == number[0]:
                    min_result += '1'
                else:
                    min_result += '0'
            else:
                min_result += number[i]
        else:
            if number[i] != '0' and number[i] != number[0]:
                min_target = number[i]
                min_result += '0'
            else:
                min_result += number[i]

    return int(max_result) - int(min_result)