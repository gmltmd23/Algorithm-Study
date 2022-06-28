"""

인덱스를 하나씩 증가시켜서 DP를 진행하는 테크닉을 익혀두자!

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
ugly_numbers = [0] * n
ugly_numbers[0] = 1

index_2 = index_3 = index_5 = 0
two, three, five = 2, 3, 5

for i in range(1, n):
    ugly_numbers[i] = min(two, three, five)
    if ugly_numbers[i] == two:
        index_2 += 1
        two = ugly_numbers[index_2] * 2
    if ugly_numbers[i] == three:
        index_3 += 1
        three = ugly_numbers[index_3] * 3
    if ugly_numbers[i] == five:
        index_5 += 1
        five = ugly_numbers[index_5] * 5

print(ugly_numbers)
