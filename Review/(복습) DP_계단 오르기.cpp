/*

(����) ���� ���� 2579�� DP_��� ������

���̵� ���ø��� ���Ѵٸ� �ð��� �����ɸ����� �����̴�.
��Ģ�� ã�� ��ȭ���� ������ Ǯ��.

*/

#include <iostream>

#define MAX 301

using namespace std;

int n;
int s[MAX], dp[MAX];

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> s[i];

	dp[0] = s[0];
	dp[1] = s[0] + s[1];
	dp[2] = max(s[1] + s[2], s[0], s[2]);
	for (int i = 3; i < n; i++)
		dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i]);
	cout << dp[n - 1] << endl;

	return 0;
}