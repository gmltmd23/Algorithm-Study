/*

(복습) 자료구조_키로거

예전에 문제를 풀때에는 password 객체를
deque로 사용했었는데, 굳이 deque까지 갈거없고, 모두 stack으로 처리해도
잘 풀리는 문제였다. 역시 실력이 발전하기는 했나보다ㅋㅋㅋㅋㅋ

deque를 stack으로 바꿔줬으므로 그에따른 print 함수도 변경해주었다.
좋은 문제다.

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