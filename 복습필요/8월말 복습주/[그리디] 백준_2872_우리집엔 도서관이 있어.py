import sys
input = sys.stdin.readline

n = int(input())
books = []
for i in range(n):
    books.append(int(input()))

targetMaxValue = n
while books:
    nowValue = books.pop()
    if nowValue == targetMaxValue:
        targetMaxValue -= 1

print(targetMaxValue)