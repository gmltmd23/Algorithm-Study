/*

���� ���� 13417�� �׸���_ī�� ���ڿ�

���� �ڵ��׽�Ʈ ���� 2������ ���ø��� ��������.
�׸������̱��ѵ�, �ڷᱸ���ʿ� �� ����� �����̴�.

�ܼ��� ���� �������� �˰� vector ���� STL�� ����Ѵٸ� Ǯ������.
ũ��� + deque �ڷᱸ���� �̿����� �˸� ����Ǯ���ִ�.

deque�� �켱 ù��°���� �־����,
deque.front() ���� �������� ���Ͽ� �װͺ��� ������ �����ų� ������
���ʿ� �����͸� �����ϰ� �׷��������� ���ʿ� �����͸� �����ϸ� Ǯ���� ��������.

*/

#include <iostream>
#include <deque>

#define endl '\n'
using namespace std;

void print(deque<char> &target) {
	for (deque<char>::iterator iter = target.begin(); iter != target.end(); iter++)
		cout << *iter;
	cout << endl;
}

int main() {
	int T, N;
	char first;
	deque<char> alphabet;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		cin >> first;
		alphabet.push_back(first);

		for (int j = 0; j < N - 1; j++) {
			char temp;
			cin >> temp;
			
			if (temp <= alphabet.front())
				alphabet.push_front(temp);
			else
				alphabet.push_back(temp);
		}

		print(alphabet);
		alphabet.clear();
	}

	return 0;
}