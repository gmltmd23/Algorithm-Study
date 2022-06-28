/*

(복습) 백준 문제 14501번 DP_퇴사

계속 진행됬던 DP값과
day에 있는 cost와 이 cost가 time동안 진행됬을때에 dp값을 비교해서 더 큰것이 최종값이되게끔 만들어주면된다.

*/

#include <iostream>
#include <algorithm>

using namespace std;

int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int dp[16] = { 0 };
	int pay[16] = { 0 };
	int time[16] = { 0 };
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> time[i] >> pay[i];
		for (int j = 0; j < i; j++) {
			if (time[j] + j <= i && i + time[i] <= n + 1) {
				dp[i] = max(dp[i], dp[j] + pay[i]);
			}
		}
	}
	int answer = 0;
	for (int i = 0; i <= n; i++) {
		answer = max(answer, dp[i]);
	}
	cout << answer;


	return 0;
}