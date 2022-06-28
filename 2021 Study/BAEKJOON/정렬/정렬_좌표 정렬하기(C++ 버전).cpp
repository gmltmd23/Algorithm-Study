/*

���� ���� 11650�� ��ǥ �����ϱ�

C++ STL algorithm ����� �ִ� sort�� �⺻������ quick sort�� �����Ǿ� �־ ���ϴ�.
�׸��� ����Ҷ����� endl�� �����������.
������ �����⶧���� '\n'�� ����ؾ��Ѵ�.

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<pair<int, int>> arr;

	int x, y;
	for (int i = 0; i < n; i++) {
		cin >> x;
		cin >> y;

		arr.push_back(make_pair(x, y));
	}
	sort(arr.begin(), arr.end());

	for (int i = 0; i < n; i++) {
		cout << arr[i].first << ' ' << arr[i].second << "\n";
	}

	return 0;
}