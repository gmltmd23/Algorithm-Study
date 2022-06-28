"""

문제 1543 문서 검색

복잡한 KMP 알고리즘 같은거를 쓰지말고,
그냥 시간복잡도가 O(n)이 나오게끔 알고리즘을 짜서
풀면 간단하게 풀리는 문제이다.

문제에서 힌트를 주는데, 중복이 없게끔 하라는 부분이 시간을 단축시키는 요령이다.
만약 target 문자열이 string 문자열 안에 존재한다면, 그 이후에 발견되야 될 target 문자열들은
중복이 발생하면 안되니깐 start, end 인덱스가 target 문자열의 길이만큼 점프한곳에서 부터
다시 string 문자열을 탐색해주면 중복이 발생할일이 없다.

"""

import sys
input = sys.stdin.readline

def main():
    string, target = input().rstrip(), input().rstrip()
    start, end = 0, (len(target) - 1)
    count = 0
    while end < len(string):
        if string[start : end + 1] == target:
            count += 1
            start, end = (start + len(target)), (end + len(target))
        else:
            start, end = (start + 1), (end + 1)
    print(count)
main()