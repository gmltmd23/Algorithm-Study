/*

���� ���� 2873��

��Ȯ���� �°����� �޸� �ʰ��� ����
�ڵ� ����� ���� �ʴ´�.
�ٽ��� ����� �ִ�� ������ �����ϱ� �鸱�� �ִ� ĭ�� ��� �� ����� �ִ�� ����� �Ǵ°��̴�.

�� ������ 3���� ���� ������ Ǯ��ȴ�.
1. r�� Ȧ���ΰ��
2. c�� Ȧ���ΰ��
3. r, c �Ѵ� ¦���ΰ��

1��, 2���� ������ ��� ĭ�� �� �鸮�� ����� �ֱ⿡ �� ������ �����ʴ´�.
3�� �Ѵ� ¦���ΰ�찡 �߿��ϴ�.

¦���� ����϶� �ùķ��̼��� ��������
��� ���� ������ ���ĭ���� �� 1ĭ�� ������ ���Եȴ�.
������ �׷��� �Ǿ��ִ�.

������ ���ǿ� �°Բ� Ǯ������ �� 1ĭ �������³��� ���� ���� ���ڸ� �Ǵ°��̴�.
�׷��� ����س� ����� ó��(0, 0)���� ��ŸƮ �Ҷ� (0, 1)�� �ȵ鸮�ų�, (1, 0)�� �ȵ鸮�°��
�� �� ������ (r - 1, c - 1)�� �����ϱ��� (r - 1, c - 2)�� �ȵ鸮�ų�, (r - 2, c - 1)�� �ȵ鸮�� ���

�̷��� 4���� ��쿡 ���缭 �ڵ带 ��������.
�ٵ� �� ������δ� �޸� �ʰ��� �߻��Ͽ� ����� �����ʴ´�.

�Ƹ��� �� 4���� ��츻�� ������� original �߰��뿡 ���� ���� ���� ������ element�� �������
�װ��� ���ذ��°��� ���ϴ°� ����.

���� �� ����غ��� �ڵ带 �����ؾ��ҰͰ���.

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