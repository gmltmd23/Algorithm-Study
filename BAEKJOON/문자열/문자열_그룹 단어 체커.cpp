/*

���� ���� 1316�� ���ڿ�_�׷� �ܾ� üĿ

���� �ڵ��׽�Ʈ 1���� ���� ���ù��� �����̴�.
���� ������ �߼��� �׷����� ����ٵ簡, Ʈ�������ٵ簡 ���ٴ�
��κ� ���������� ���� ���´�.

�׷��� ����, �׸��� ���ַ� �����صδ°��� ����� ���� ����̴�.
������ϱ� 1�������� �� Ǯ��߰ڴ�.

*/

#include <iostream>
#include <set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	int answer = n;
	for (int i = 0; i < n; i++) {
		set<char> checker;
		string word;
		cin >> word;

		char before_word = word[0];
		for (char c : word) {
			if (checker.find(c) == checker.end()) {
				checker.insert(c);
				before_word = c;
			}
			else {
				if (before_word != c) {
					answer--;
					break;
				}
			}
		}
	}

	cout << answer << endl;

	return 0;
}