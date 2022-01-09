/*

(복습) 그리디_만들 수 없는 금액

아이디어가 중요했던 문제이다.
예전에는 파이썬으로 풀었었는데 C++로 하니깐 확실히 코드가 길어지는 면이 있다.
이런게 좋은 그리디 문제라고 생각한다.

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;

int main(void)
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	vector<int> coins(n);
	for (int i = 0; i < n; i++)
		cin >> coins[i];
	sort(coins.begin(), coins.end());
	
	int target = 1;
	for (int x : coins)
	{
		if (target < x)
			break;
		target += x;
	}

	cout << target << endl;

	return 0;
}