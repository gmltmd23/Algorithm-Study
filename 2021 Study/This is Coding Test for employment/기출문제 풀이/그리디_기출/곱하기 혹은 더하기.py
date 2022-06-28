import sys
input = sys.stdin.readline

numbers = list(input().rstrip())
result = 0
for number in numbers:
    op = '*'
    if int(number) <= 1 or result <= 1:
        op = '+'
    result = eval(op.join([str(result), str(number)]))

print(result)