/*

(����) ���� ���� 11052�� DP_ī�� �����ϱ�

������ Ǯ������� ������� ���淡 ������ �˾Ҵµ�
�� ������ �ؾ��߾��� ������ ����Ѵ�.
���� ������.

*/

#include <iostream>
#include <vector>

using namespace std;

int n;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	vector<int> dp;
	vector<int> p;
	p.resize(n);

	dp.resize(n + 1);
	for (int i = 1; i < n + 1; i++)
	{
		for (int j = 1; j < i + 1; j++)
		{
			dp[i] = max(dp[i], dp[i - j] + p[j - 1]);
		}
	}

	cout << dp[n] << endl;
	
	return 0;
}