import sys
input = sys.stdin.readline

n = int(input())
result = []
for order in range(n):
    age, name = input().split()
    result.append([int(age), name, order])
result.sort(key = lambda x: (x[0], x[2]))

answer = ""
for age, name, order in result:
    answer += "{0} {1}\n".format(age, name)
print(answer, end = '')