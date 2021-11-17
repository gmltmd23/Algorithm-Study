#include <iostream>
#include <stack>
#include <deque>

using namespace std;

void print_deque(deque<char> st) {
	for (deque<char>::iterator iter = st.begin(); iter != st.end(); iter++)
		cout << *iter;
	cout << "\n";
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int test_case;
	cin >> test_case;

	for (int count = 0; count < test_case; count++) {
		string origin;
		cin >> origin;
		
		deque<char> password;
		stack<char> save;
		for (char c : origin) {
			if ((c == '<') || (c == '>') || (c == '-')) {
				switch (c) {
				case '<':
					if (!(password.empty())) {
						save.push(password.back());
						password.pop_back();
					}
					break;
				case '>':
					if (!(save.empty())) {
						password.push_back(save.top());
						save.pop();
					}
					break;
				case '-':
					if (!(password.empty()))
						password.pop_back();
					break;
				default:
					break;
				}
			}
			else
				password.push_back(c);
		}
		while (!save.empty()) {
			password.push_back(save.top());
			save.pop();
		}
		print_deque(password);
	}

	return 0;
}