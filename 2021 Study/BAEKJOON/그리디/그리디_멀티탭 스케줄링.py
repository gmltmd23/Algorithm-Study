"""

백준 문제 1700번 그리디_멀티탭 스케줄링

거의 다 맞춘 문제인데, appliances와 multi_tap에서 일치하는것을 찾는 과정중
멀티탭의 개수만큼만 찾는줄 알았는데, appliances 끝까지 찾아줘야 하는거을 빼먹어서 계속 틀렸던 문제이다.

이 문제의 중요점은 분기점을 잘 나누는것이다.

1. 멀티탭에 비어있는 구멍이 있을경우 = 걍 꽂으면 된다.
2. 멀티탭에 꽂으려고 보니 이미 그 전자제품이 꽂혀있는 경우 = 아무것도 안해도 된다.
3. 멀티탭이 꽉찬 경우 = 무엇을 뽑아버릴지 골라야 된다. 즉 향후 사용할 예정이 있는 전자기기를 안뽑으면 되는것이다.
만약 모두 사용할 예정이 있다면 아무거나 뽑아도 된다.

복습하자.

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
appliances = list(map(int, list(input().split())))
multi_tap = []

answer = 0
for i in range(len(appliances)):
    if appliances[i] in multi_tap:
        continue
    if len(multi_tap) < n:
        multi_tap.append(appliances[i])
        continue

    answer += 1
    out = idx = 0
    for j in range(n):
        try:
            temp_idx = appliances[i + 1:].index(multi_tap[j])
            if temp_idx > idx:
                out, idx = j, temp_idx
        except:
            out = j
            break
    multi_tap[out] = appliances[i]

print(answer)