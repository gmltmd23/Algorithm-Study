/*

(����) ���� ���� 7570�� DP_�� �����

������ Ǯ������ ������ �����̴�.
DP ��Ʈ���� �����µ� ���Ҵ� �����̴�.

������ ���۵Ǽ� ������ �Ÿ��� ������, ������ �ؾ߰ڴ� ^___^

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