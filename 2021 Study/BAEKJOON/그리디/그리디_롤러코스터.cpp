/*

백준 문제 2873번

정확도는 맞겠지만 메모리 초과로 인해
코드 통과가 나지 않는다.
핵심은 기쁨을 최대로 만들라고 했으니깐 들릴수 있는 칸은 모두 다 들려서 최대로 만들면 되는것이다.

이 문제는 3가지 경우로 나눠서 풀면된다.
1. r이 홀수인경우
2. c가 홀수인경우
3. r, c 둘다 짝수인경우

1번, 2번은 무조건 모든 칸을 다 들리는 방법이 있기에 별 문제가 되지않는다.
3번 둘다 짝수인경우가 중요하다.

짝수인 경우일때 시뮬레이션을 돌려보면
어떻게 길을 가더라도 모든칸에서 단 1칸은 갈수가 없게된다.
구조가 그렇게 되어있다.

문제의 조건에 맞게끔 풀으려면 단 1칸 갈수없는놈이 가장 작은 숫자면 되는것이다.
그래서 고안해낸 방법은 처음(0, 0)에서 스타트 할때 (0, 1)을 안들리거나, (1, 0)을 안들리는경우
또 맨 마지막 (r - 1, c - 1)에 도달하기전 (r - 1, c - 2)을 안들리거나, (r - 2, c - 1)를 안들리는 방법

이렇게 4가지 경우에 맞춰서 코드를 만들어줬다.
근데 이 방법으로는 메모리 초과가 발생하여 통과가 되지않는다.

아마도 저 4가지 경우말고 예를들어 original 중간쯤에 가장 작은 값을 가지는 element가 있을경우
그곳을 피해가는것을 원하는것 같다.

조금 더 고민해보고 코드를 수정해야할것같다.

*/

#include <iostream>
#include <algorithm>

#define MAX 1000
#define endl '\n'

using namespace std;

int r, c;
int original[MAX][MAX];

void input() {
	cin >> r >> c;
	for (int x = 0; x < r; x++) {
		for (int y = 0; y < c; y++) {
			cin >> original[x][y];
		}
	}
}

void r_is_odd(string &answer) {
	for (int x = 0; x < r; x++) {
		for (int y = 0; y < (c - 1); y++) {
			if (x % 2 == 0)
				answer += 'R';
			else
				answer += 'L';
		}
		if (x != (r - 1)) answer += 'D';
	}
}

void c_is_odd(string &answer) {
	for (int y = 0; y < c; y++) {
		for (int x = 0; x < (r - 1); x++) {
			if (y % 2 == 0)
				answer += 'D';
			else
				answer += 'U';
		}
		if (y != (c - 1)) answer += 'R';
	}
}

void all_is_even(string &answer) {
	int temp[] = { original[0][1], original[1][0], original[r - 2][c - 1], original[r - 1][c - 2] };
	sort(temp, temp + 4);
	int minimum = temp[0];
	if (minimum == original[0][1]) { // no_start_right
		answer = "DR";
		if (c > 2) {
			answer += "RU";
			for (int i = 0; i < c - 3; i++) {
				answer += 'R';
				if (i % 2 == 0)
					answer += 'D';
				else
					answer += 'U';
			}

			answer += 'D';
			for (int x = 2; x < r; x++) {
				for (int y = 0; y < c - 1; y++) {
					if (x % 2 == 0)
						answer += 'L';
					else
						answer += 'R';
				}
				if (x != r - 1)
					answer += 'D';
			}
		}
		return;
	}
	if (minimum == original[1][0]) { // no_start_down
		answer = "RD";
		if (r > 2) {
			answer += "DL";
			for (int i = 0; i < r - 3; i++) {
				answer += 'D';
				if (i % 2 == 0)
					answer += 'R';
				else
					answer += 'L';
			}

			answer += 'R';
			for (int y = 2; y < c; y++) {
				for (int x = 0; r - 1; x++) {
					if (y % 2 == 0)
						answer += 'U';
					else
						answer += 'D';
				}
				if (y != c - 1)
					answer += 'R';
			}
		}
		return;
	}
	if (minimum == original[r - 2][c - 1]) { // no_last_up
		for (int x = 0; x < r - 2; x++) {
			for (int y = 0; y < c - 1; y++) {
				if (x % 2 == 0)
					answer += 'R';
				else
					answer += 'L';
			}
			answer += 'D';
		}

		for (int i = 0; i < c - 1; i++) {
			if (i % 2 == 0)
				answer += 'D';
			else
				answer += 'U';
			answer += 'R';
		}
		return;
	}
	if (minimum == original[r - 1][c - 2]) { // no_last_left
		for (int y = 0; y < c - 2; y++) {
			for (int x = 0; x < r - 1; x++) {
				if (y % 2 == 0)
					answer += 'D';
				else
					answer += 'U';
			}
			answer += 'R';
		}

		for (int i = 0; i < r - 1; i++) {
			if (i % 2 == 0)
				answer += 'R';
			else
				answer += 'L';
			answer += 'D';
		}
		return;
	}
}

string solution() {
	string answer = "";
	if (r % 2 == 0)
		if (c % 2 == 0)
			all_is_even(answer);
		else
			c_is_odd(answer);
	else
		r_is_odd(answer);

	return answer;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	input();
	cout << solution() << endl;

	return 0;
}