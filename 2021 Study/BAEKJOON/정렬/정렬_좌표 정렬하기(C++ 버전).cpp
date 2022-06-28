/*

백준 문제 11650번 좌표 정렬하기

C++ STL algorithm 헤더에 있는 sort는 기본적으로 quick sort로 구현되어 있어서 편리하다.
그리고 출력할때에는 endl를 사용하지마라.
굉장히 느리기때문에 '\n'를 사용해야한다.

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