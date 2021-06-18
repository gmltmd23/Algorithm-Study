"""

HackerRank BitWise문제

a = [29, 36, 57]
b = [25, 18, 3]
-> [85, 99, 0]

a = [4, 3, 57]
b = [2, 4, 49]
-> [11, 0, 167]


"""

def bitwiseEquations(a, b): # 0 <= x, y  [x, y는 0과 양의 정수]
    result, length = [], len(a)
    for idx in range(length):
        sub_value = a[idx] - b[idx]
        if sub_value >= 0:
            if sub_value % 2 == 0: # 짝수
                x = sub_value // 2
                y = a[idx] - x
                if (x ^ y) == b[idx]:
                    result.append((2 * x) + (3 * y))
                else:
                    result.append(0)
            else: # 홀수
                result.append(3 * a[idx])
        else:
            result.append(0)
    return result

a = [4, 3, 57]
b = [2, 4, 49]
print(bitwiseEquations(a, b))
