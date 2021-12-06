/*

백준 문제 1448번 그리디_삼각형 만들기

문제를 풀기에 앞서 삼각형을 만드는 조건을 알아야 한다.
삼각형을 이루는 세 변의 길이를 알고 있다고 하자. (a, b, c 이렇게 세 변)
c를 가장 긴 변이라고 할 경우에 (c < (a + b))를 만족시키면 삼각형은 만들어진다.

위 조건을 만족시키지 못한다면 삼각형을 만들 수 없다.
저것에 맞게끔 코드를 짜주면된다.

푸는 방법으로서는 sort를 해서 가장 큰 값들부터 써먹는 방법 또는,
애초에 큰값들 먼저 나오게끔 우선순위큐(heapq 최대힙)를 써도 된다.

나는 최대힙을 사용해서 풀었다.

*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int pop(priority_queue<unsigned int> &q) {
	unsigned int temp = q.top();
	q.pop();
	return temp;
}

int solution(priority_queue<unsigned int> q) {
	unsigned int c, b = pop(q), a = pop(q);
	while (!q.empty()) {
		c = b, b = a, a = pop(q);
		if (c < (a + b))
			return (a + b + c);
	}

	return -1;
}

int main() {
	int n;
	cin >> n;

	priority_queue<unsigned int> candidate;
	int temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		candidate.push(temp);
	}

	cout << solution(candidate) << endl;

	return 0;
}