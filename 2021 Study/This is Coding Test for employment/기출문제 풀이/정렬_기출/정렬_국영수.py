import sys
input = sys.stdin.readline

n = int(input().rstrip())
students = []
for i in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    students.append((name, kor, eng, math))
students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])