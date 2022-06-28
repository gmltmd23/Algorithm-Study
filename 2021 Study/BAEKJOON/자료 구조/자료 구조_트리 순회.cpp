/*

���� ���� 1991�� �ڷ� ����_Ʈ�� ��ȸ

C++ ���ΰ�, Ʈ�� ��ȸ ���� �� �ڵ带 ¥���Ҵ�.
����, ����, ���� ��ȸ�� �Ҷ� �ܾ��� �ǹ̿� �����ϸ�
Ʈ���� ��ȸ�� ����� ���� �� �ִ�.

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