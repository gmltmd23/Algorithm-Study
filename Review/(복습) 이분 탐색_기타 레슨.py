"""

백준 문제 2343번 이분 탐색_기타 레슨

정답률 30.712%의 높은 난이도의 문제이다.
범위가 매우 넓다는 점에서 이분 탐색이라고 눈치는 챌 수 있었지만
푸는 방법이 떠오르지 않아서, 인터넷을 참고하여 공부해보았다.

일단 이분 탐색 대부분의 문제가 이렇다.
1. start, end 값을 구하라 (보통 start가 최소값, end를 최대값으로 정하는 경우가 많다.)
2. 이분 탐색 조건을 만들어라
3. mid 값을 기준으로 start, end를 움직여라
4. 답을 구하라

저 4가지 과정을 거쳐서 문제를 풀 수가 있는데, 자주 나오는 유형은 아니더라도
확실히 연습이 필요하다. 코테에 나오면 엄청 당황할거 같다.

이 문제또한 저 위의 과정대로 문제를 풀어보자면..
1. start, end = max(lectures), sum(lectures)이다. 참고로 start와 end는 여기서 블루레이 디스크의 크기를 의미한다.
이것의 의미는 start는 블루레이 크기의 최소값이니 블루레이 디스크가 n=m인 경우를 말하는것이고
end는 최대값이니 모든 영상을 다 포함하는 즉 블루레이 디스크의 개수 m이 1인 경우이다.

2. 이분 탐색 조건은 이제 mid값을 기준으로 lectures 배열을 처음부터 더하여
경계선(div)의 값이 m이하 인지 아닌지를 따져준다.

만약 div가 m이하라면, div가 부족하다는 뜻(주어진 블루레이 디스크 m개를 맞춰야함)이다.
다시 말하자면 최대값 end를 줄여서 mid값을 낮춰줘야 div개수가 늘어난다.

만약 div가 m보다 크다면 div가 많다는 뜻이니깐, start를 높여 mid값을 높여줘야 div 개수를 줄일수가 있다.

3. 위에 방식을 이용하여 start, end값을 조절한다.

4. 최종적으로는 mid가 answer이 된다.

다 보고나서도 이해가 약간 힘들었지만, 복습을 해서 내껄로 만들어야겠다.
꼭 복습하자.


"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))
start, end = max(lectures), sum(lectures)

while start <= end:
    mid = (start + end) // 2
    limit, div = 0, 1
    for i in range(n):
        limit += lectures[i]
        if limit > mid:
            div += 1
            limit = lectures[i]

    if div <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)