/*

백준 문제 7570번 DP_줄 세우기

문제를 보았을때 LIS를 쓰면 된다는것을 알긴했는데,
LIS 자체를 오랜만에 봐서 구현법을 까먹어서 1시간정도 애를먹다가 결국 풀이를 보았다.
자주 나오는 문제가 아니라 등한시한게 문제가 됬던 문제이다.

다만 이 LIS문제는 예를들어 2 5 3 4 1 일때,
2 3 4 이렇게 찾는것이 아니고, 서로 인덱스가 바로 옆인애들만 LIS로 쳐줘야 한다.
즉 이미 정렬이 되있어서 건드릴 필요없는 애들을 찾는것이다.
이 문제 기준으로는 LIS는 3 4 가 되는것이다.

그러면 전체 아이의 수 N에서 LIS 수를 빼게되면 정렬의 필요성이 있는 아이들의 수가 나온다.
답은 그럼 N - LIS가 될것이다.

복습하자. 그리고 백준 문제 2631번도 풀어보자 비슷한 문제이다.

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