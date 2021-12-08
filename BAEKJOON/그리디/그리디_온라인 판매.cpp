/*

���� ���� 1246�� �׸���_�¶��� �Ǹ�

������ �ؿ� �������� ������ ��� ������ �׷��� ������ �� ������ �κ��� �־���.
���̵� ��ü�� ���� ������ �ƴϴ�.

�������� �����ϰ� Ǯ��Ǵµ� �߿��Ѱ���
����� ������ �Ѿ�Բ� ����� �ȼ��� ���ٴ� ���̰�,
�ѹ� �Ⱦ��� ������Դ� �� ����� �ȼ��� ���°��� ����ϰ� �ڵ带 ¥��ȴ�.

*/

#include <iostream>
#include <algorithm>
#include <vector>

#define endl '\n'
using namespace std;

int n, m;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;
	vector<int> prices;
	for (int i = 0; i < m; i++) {
		unsigned int temp;
		cin >> temp;
		prices.push_back(temp);
	}
	sort(prices.rbegin(), prices.rend());

	unsigned int total = 0;
	int p = 0;
	for (int i = 0; i < n; i++) {
		if (prices[i] * (i + 1) > total) {
			total = prices[i] * (i + 1);
			p = prices[i];
		}
	}

	cout << p << " " << total << endl;

	return 0;
}