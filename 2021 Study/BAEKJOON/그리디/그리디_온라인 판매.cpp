/*

백준 문제 1246번 그리디_온라인 판매

문제가 해외 문제에서 번역이 됬던 문제라 그런지 설명이 좀 난해한 부분이 있었다.
난이도 자체는 높은 문제는 아니다.

내림차순 정렬하고 풀면되는데 중요한것은
계란의 갯수를 넘어가게끔 계란을 팔수가 없다는 점이고,
한번 팔아준 사람에게는 또 계란을 팔수가 없는것을 명시하고 코드를 짜면된다.

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