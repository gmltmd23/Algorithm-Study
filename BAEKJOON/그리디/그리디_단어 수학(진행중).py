"""

첫번째로 제출한 코드인데 틀렸다.. 테스트케이스는 모두 통과하는데 틀린거보면 효율성이 별로인거같다.
아마도 문자열 '0'을 추가하는 과정때문에 틀리다고 나온거같은데,
저것을 없애봐야겠다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
alphabet = [-1] * 26 # 알파벳 개수가 26개임
arr, numbers = [], [k for k in range(10)]
total = 0
for i in range(n):
    arr.append(input().rstrip())
arr.sort(key = lambda x: len(x), reverse = True)
max_length = len(arr[0])
for i in range(n):
    if len(arr[i]) < max_length:
        arr[i] = ('0' * (max_length - len(arr[i]))) + arr[i] # 빈공간을 문자열 0으로 채워준다

for char in range(max_length):
    for i in range(n):
        if arr[i][char] != '0':
            index = ord(arr[i][char]) % 65
            if alphabet[index] == -1:
                alphabet[index] = numbers.pop()
            total += (10 ** (max_length - 1 - char)) * alphabet[index]
print(total)