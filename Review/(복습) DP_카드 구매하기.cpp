/*

(복습) 백준 문제 11052번 DP_카드 구매하기

예전에 풀었을당시 정답률이 높길래 쉬운줄 알았는데
꽤 생각을 해야했었던 문제로 기억한다.
좋은 문제다.

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