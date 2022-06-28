/*

(복습) 백준 1010번 DP_다리 놓기

dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1] 의 점화식을 이용해서 푸는 문제이다.
여기서 dp[n][m - 1]은 dp[n][m]의 바로 전 까지 dp 됬던것, 즉 바로 전까지 다리를 놓았던것을 말한다.
중요한거는 dp[n - 1][m - 1] 이거인데 다리를 놓을때 한놈의 다리를 고정시켜놓고 나머지를 움직이는 경우라고 생각하면 된다.
그럼 끝이다.

팩토리얼식으로 만들어도 풀리긴한다.

*/

#include <iostream>

#define MAX 30
using namespace std;

int t;
int dp[MAX][MAX];

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> t;
	for (int i = 0; i < MAX; i++)
	{
		for (int j = 0; j < MAX; j++)
		{
			if (i == 1)
				dp[i][j] = j;
			else if (i == j)
				dp[i][j] = 1;
			else
				dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
		}
	}

	int n, m;
	for (int i = 0; i < t; i++)
	{
		cin >> n >> m;
		cout << dp[n][m] << endl;
	}

	return 0;
}