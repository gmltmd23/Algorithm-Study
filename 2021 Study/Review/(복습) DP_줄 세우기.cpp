/*

(복습) 백준 문제 7570번 DP_줄 세우기

얼마전에 풀었었던 문제의 복습이다.
DP 컨트롤을 익히는데 좋았던 문제이다.

인턴이 시작되서 공부할 거리가 많은데, 열심히 해야겠다 ^___^

*/

#include <iostream>

#define endl '\n'

using namespace std;

int N, X, answer;
int dp[1000001];

int main() {
	ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> X;
		dp[X] = dp[X - 1] + 1;
		answer = max(answer, dp[X]);
	}

	cout << N - answer << endl;

	return 0;
}