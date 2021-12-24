/*

(복습) 백준 문제 2839번 그리디_설탕 배달

정답률 34%의 그리디 문제이다.
복습으로 푸는거라 그런지 바로 풀리긴 했다.

이 문제는 단순하다.
5로 나누어떨어지면 answer에다가 (n / 5)를 확 더해서 끝내주면되고,
그렇지 않다면 계속 -3을 해주면서 카운팅을 해주면 된다.

결과값만 n >= 0일 때로 구분하여 잘 출력해주면 끝

*/

#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	
	int answer = 0;
	while (n >= 0) {
		if (n % 5 == 0) {
			answer += (n / 5);
			break;
		}
		n -= 3;
		answer++;
	}

	if (n >= 0)
		cout << answer << '\n';
	else
		cout << -1 << '\n';

	return 0;
}