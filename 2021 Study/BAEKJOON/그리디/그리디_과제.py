default = [6, 5, 3, 1, 8, 7, 2, 4]

count = int(input())
temp = []
for i in range(count):
    temp.append(int(input()))

"""
# 선택정렬
for i in range(len(temp) - 1):
    min_idx = i
    for j in range(i + 1, len(temp)):
        if temp[j] < temp[min_idx]:
            min_idx = j
    temp[i], temp[min_idx] = temp[min_idx], temp[i]
"""


"""
# 버블정렬
for i in range(len(temp) - 1):
    for j in range(len(temp) - i - 1):
        if temp[j] > temp[j + 1]:
            temp[j], temp[j + 1] = temp[j + 1], temp[j]
"""

"""
# 삽입정렬
for end in range(1, len(temp)):
    for i in range(end, 0 , -1):
        if temp[i] < temp[i - 1]:
            temp[i], temp[i - 1] = temp[i - 1], temp[i]
"""

# 합병정렬


# 퀵정렬

# 힙정렬

print(temp)