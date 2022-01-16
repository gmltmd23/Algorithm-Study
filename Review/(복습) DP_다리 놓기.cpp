/*

(����) ���� 1010�� DP_�ٸ� ����

dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1] �� ��ȭ���� �̿��ؼ� Ǫ�� �����̴�.
���⼭ dp[n][m - 1]�� dp[n][m]�� �ٷ� �� ���� dp �����, �� �ٷ� ������ �ٸ��� ���Ҵ����� ���Ѵ�.
�߿��ѰŴ� dp[n - 1][m - 1] �̰��ε� �ٸ��� ������ �ѳ��� �ٸ��� �������ѳ��� �������� �����̴� ����� �����ϸ� �ȴ�.
�׷� ���̴�.

���丮������� ���� Ǯ�����Ѵ�.

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