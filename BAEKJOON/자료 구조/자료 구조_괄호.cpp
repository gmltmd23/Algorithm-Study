/*

백준 문제 9012번 자료 구조_괄호

큰 대분류는 문자열로 구분되어있는 문제인데, 문자열보다는
스택의 쓰임새를 사용하는 문제이다 이건

스택을 2개를 쓰겠다는 생각만하면 쉽게 풀 수 있는 문제이다.
다만 flag를 사용하지않고 더 이쁘게 푸는방법이 있긴할텐데, 시간효율성에서 차이가 나지않으니
이 코드도 괜찮은것 같다.

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