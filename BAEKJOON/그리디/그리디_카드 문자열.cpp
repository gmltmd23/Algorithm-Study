/*

백준 문제 13417번 그리디_카드 문자열

뭔가 코딩테스트 문제 2번으로 나올만한 문제였다.
그리디문제이긴한데, 자료구조쪽에 더 가까운 문제이다.

단순한 정렬 문제인줄 알고 vector 같은 STL을 사용한다면 풀수없다.
크기비교 + deque 자료구조를 이용할줄 알면 쉽게풀수있다.

deque에 우선 첫번째값을 넣어놓고,
deque.front() 값을 기준으로 비교하여 그것보다 순서가 빠르거나 같으면
앞쪽에 데이터를 삽입하고 그렇지않으면 뒤쪽에 데이터를 삽입하면 풀리는 문제였다.

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