/*

(����) �׸���_���� �� ���� �ݾ�

���̵� �߿��ߴ� �����̴�.
�������� ���̽����� Ǯ�����µ� C++�� �ϴϱ� Ȯ���� �ڵ尡 ������� ���� �ִ�.
�̷��� ���� �׸��� ������� �����Ѵ�.

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