import sys
input = sys.stdin.readline

n = int(input().rstrip())
stages = list(map(int, input().split()))
failure_rates, people = [0] * (n + 2), len(stages)
for stage in stages:
    failure_rates[stage] += 1

for i in range(1, n + 1):
    bunmo = people
    people -= failure_rates[i]
    failure_rates[i] = ((failure_rates[i] / bunmo), i)

for item in sorted(failure_rates[1 : (n + 1)], key = lambda x: x[0], reverse = True):
    print(item[1], end = ' ')