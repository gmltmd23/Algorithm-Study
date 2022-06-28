/*

(����) �ڷᱸ��_Ű�ΰ�

������ ������ Ǯ������ password ��ü��
deque�� ����߾��µ�, ���� deque���� ���ž���, ��� stack���� ó���ص�
�� Ǯ���� ��������. ���� �Ƿ��� �����ϱ�� �߳����٤���������

deque�� stack���� �ٲ������Ƿ� �׿����� print �Լ��� �������־���.
���� ������.

*/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void print_stack(stack<char> st) {
	vector<char> temp;
	temp.reserve(st.size());
	while (false == st.empty()))
	{
		temp.push_back(st.top());
		st.pop();
	}

	for (vector<char>::iterator iter = temp.end(); iter != temp.begin(); --iter)
		cout << *iter;
	cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int test_case;
	cin >> test_case;

	for (int count = 0; count < test_case; count++) {
		string origin;
		cin >> origin;
		
		stack<char> password;
		stack<char> save;
		for (char c : origin) {
			if ((c == '<') || (c == '>') || (c == '-')) {
				switch (c) {
				case '<':
					if (false == (password.empty())) {
						save.push(password.top());
						password.pop();
					}
					break;
				case '>':
					if (false == (save.empty())) {
						password.push(save.top());
						save.pop();
					}
					break;
				case '-':
					if (false == (password.empty()))
						password.pop();
					break;
				default:
					break;
				}
			}
			else
				password.push(c);
		}
		while (!save.empty()) {
			password.push(save.top());
			save.pop();
		}
		print_deque(password);
	}

	return 0;
}