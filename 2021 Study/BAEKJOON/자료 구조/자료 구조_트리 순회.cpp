/*

백준 문제 1991번 자료 구조_트리 순회

C++ 공부겸, 트리 순회 공부 겸 코드를 짜보았다.
전위, 중위, 후위 순회를 할때 단어의 의미에 집중하면
트리의 순회를 까먹지 않을 수 있다.

*/

#include <iostream>

#define endl "\n"
#define MAX 26
#define IDX(x) (x - 'A')

using namespace std;

pair<int, int> edges[MAX];

void pre_order(char now) {
	if (now != '.') {
		cout << now;
		pre_order(edges[IDX(now)].first);
		pre_order(edges[IDX(now)].second);
	}
}

void in_order(char now) {
	if (now != '.') {
		in_order(edges[IDX(now)].first);
		cout << now;
		in_order(edges[IDX(now)].second);
	}
}

void post_order(char now) {
	if (now != '.') {
		post_order(edges[IDX(now)].first);
		post_order(edges[IDX(now)].second);
		cout << now;
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		char root, left, right;
		cin >> root >> left >> right;

		edges[root - 'A'].first = left;
		edges[root - 'A'].second = right;
	}

	pre_order('A');
	cout << endl;

	in_order('A');
	cout << endl;

	post_order('A');
	cout << endl;

	return 0;
}