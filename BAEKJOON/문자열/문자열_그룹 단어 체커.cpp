/*

백준 문제 1316번 문자열_그룹 단어 체커

뭔가 코딩테스트 1번에 많이 나올법한 문제이다.
요즘 코테의 추세가 그래프를 만든다든가, 트리를쓴다든가 보다는
대부분 구현문제로 많이 나온다.

그래서 구현, 그리디 위주로 연습해두는것이 상당히 좋은 방법이다.
쉬운문제니깐 1문제정도 더 풀어야겠다.

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