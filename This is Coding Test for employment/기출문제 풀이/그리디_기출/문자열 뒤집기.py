import sys
input = sys.stdin.readline

space = 0
data = input().strip()
base = '0' if data[0] == '0' else '1'

for i in range(len(data)): # base가 아니면 공백인것
    if data[i] != base:
        if data[i - 1] == base:
            space += 1

print(1 if space == 0 else space)

"""
답지에는 모두 0으로 바꿀때의 경우, 모두 1로 바꿀때의 경우라고 써놨는데
내가 생각해본 경우는
첫번째값을 기준값으로 잡고 그 이후 인덱스부터 차례로 보는데
data[i]의 값이 기준값과 다르면 공백으로 여기면 된다.

어차피 배열의 모든값을 살펴보기때문에 시간복잡도는 O(n)으로 동일하다.
"""