"""

문제 1110 더하기 사이클

어려운 문제는 아니다만,
배열을 사용하면 깔끔하게 풀수있는 문제라서 발상의 전환이 살짝 필요한 구현문제였다.

"""

import sys
input = sys.stdin.readline

numbers, result = [input().rstrip()], 100

while int(numbers[0]) != int(result):
    if len(numbers[-1]) == 1:
        numbers[-1] = '0' + numbers[-1][-1]
    result = numbers[-1][-1] + str(sum(map(lambda x: int(x), numbers[-1])))[-1]
    numbers.append(result)
print(len(numbers) - 1)