/*

���� ���� 9012�� �ڷ� ����_��ȣ

ū ��з��� ���ڿ��� ���еǾ��ִ� �����ε�, ���ڿ����ٴ�
������ ���ӻ��� ����ϴ� �����̴� �̰�

������ 2���� ���ڴٴ� �������ϸ� ���� Ǯ �� �ִ� �����̴�.
�ٸ� flag�� ��������ʰ� �� �̻ڰ� Ǫ�¹���� �ֱ����ٵ�, �ð�ȿ�������� ���̰� ����������
�� �ڵ嵵 �������� ����.

*/

#include <iostream>
#include <stack>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n;
	cin >> n;

	bool flag = false;
	for (int i = 0; i < n; i++) {
		flag = false;
		string line;
		cin >> line;

		stack<char> main_st, sub_st;
		for (int j = 0; j < line.size(); j++)
			main_st.push(line[j]);

		while (!main_st.empty()) {
			if (main_st.top() == ')') {
				sub_st.push(main_st.top());
				main_st.pop();
			}
			else {
				if (!sub_st.empty()) {
					sub_st.pop();
					main_st.pop();
				}
				else {
					cout << "NO" << "\n";
					flag = true;
					break;
				}
			}
		}

		if (main_st.empty() && sub_st.empty())
			cout << "YES" << '\n';
		else {
			if (!flag)
				cout << "NO" << '\n';
		}
	}

	return 0;
}