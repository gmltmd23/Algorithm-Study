import sys
input = sys.stdin.readline

s = input().rstrip()
alphabet, value = [], 0
for c in s:
    if c.isalpha():
        alphabet.append(c)
    else:
        value += int(c)
alphabet.sort()
alphabet.append(str(value))
print(''.join(alphabet))