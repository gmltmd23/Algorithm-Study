import sys
input = sys.stdin.readline

n = int(input())
cars = {}
for i in range(n):
	v, w = map(int, input().split())
	carNumber = i + 1
	if v not in cars:
		cars[v] = [0, 0]
	if w > cars[v][0]:
		cars[v][0], cars[v][1] = w, carNumber
	elif w == cars[v][0] and carNumber > cars[v][1]:
		cars[v][1] = carNumber

answer = 0
for v in cars.keys():
	answer += cars[v][1]

print(answer)