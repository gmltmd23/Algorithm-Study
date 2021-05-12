"""

첫번째로 제출한 코드인데 틀렸다.. 테스트케이스는 모두 통과하는데 틀린거보면 효율성이 별로인거같다.
아마도 문자열 '0'을 추가하는 과정때문에 틀리다고 나온거같은데,
저것을 없애봐야겠다.



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

# 이 과정을 제거해보자.
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

"""


"""

'0'을 채워주는 for문 부분을 없애고, 숫자를 차례로 pop 해주는 배열은 int형 변수 하나로 바꾸었다.
그렇지만 통과가 안된다.. 뭐가문제일까



import sys
input = sys.stdin.readline

n = int(input().rstrip())
alphabet = [-1] * 26 # 알파벳 개수가 26개임
arr = []
total = 0
for i in range(n):
    arr.append(input().rstrip())
arr.sort(key = lambda x: len(x), reverse = True)
max_length = len(arr[0])

pop_number, save = 9, max_length
for char in range(max_length):
    for i in range(n):
        if len(arr[i]) >= save:
            index = ord(arr[i][0]) % 65
            if alphabet[index] == -1:
                alphabet[index] = pop_number
                pop_number -= 1
            arr[i] = arr[i][1:]
            total += (10 ** (max_length - 1 - char)) * alphabet[index]
    save -= 1
print(total)

"""


"""

인터넷에 있는 답을 참고한 코드이다.
alphabet 배열 자체를 저렇게 활용하는것은 생각하지못했었다.
내가 기존에 짰던 코드보다 조건문이 없으므로 확실히 더 효율적이고 빠르다.
더 공부하자.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr, alphabet = [], [0] * 26
for i in range(n):
    arr.append(input().rstrip())

for word in arr:
    i = 0
    while word:
        now = word[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i += 1
        word = word[:-1]
alphabet.sort(reverse = True)

answer = 0
for i in range(9, 0, -1):
    answer += i * alphabet[9 - i]
print(answer)