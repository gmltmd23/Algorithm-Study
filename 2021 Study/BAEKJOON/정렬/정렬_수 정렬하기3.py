"""

백준 10989 수 정렬하기3

메모리제한 때문에 기존의 sort 같은 함수를 사용하지 않고
계수정렬을 이용해서 정렬을 해야한다.

계수정렬을 쓰니깐 시간복잡도는 최악의 경우 O(N + K)이다.
근데 K는 무시해도 되니깐 O(N)이라고 보면 될것같다.

"""

import sys
input = sys.stdin.readline
arr = [0] * 10001

for i in range(int(input())):
    arr[int(input())] += 1

for i in range(1, len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)