/*

백준 문제 2138번 그리디_전구와 스위치

문제가 난이도가 많이 높은 그리디 문제이다.
초반에 개념이 떠오르지않아서 개념쪽만 인터넷을 참고하였다.

코드를 다 만들어놓고 보니, 다른분들의 코드와 유사해지는것 같다.
나는 개인적으로 string을 int형 배열로 바꾸고 ON/OFF를 XOR로 구현하는것이 좋아 그걸로했다만,
string을 int배열로 바꿀때 O(n)만큼의 시간을 사용하므로 조금의 시간이라도 줄이고 싶은사람은 string 그대로 사용하는게 좋다고본다.
근데 XOR쪽이 좀더 멋져보여서..

문제의 핵심은 이거다.
i번째 스위치를 누르면 i-1, i, i+1 번째 전구에 영향이 간다.
예를들어 변하기전 배열의 i번째 원소가 목표로 하는 target[i]와 같다면 그건 바꿀필요가 없겠지만
다르다면 바꿔줘야한다. 그런데 i-1번째를 바꾸려면 i번째 스위치를 누르면된다. 그게 제일 최적이니깐.

이러면 경우가 나뉜다.
0번째 스위치를 눌른경우, 안누른경우
이 두가지 경우를 나눠서 처음부터 끝까지 진행해준다면 문제가 풀린다.
나중에 복습하자.

*/

#include <iostream>
#include <string>

#define MAX 987654321
#define endl '\n'

using namespace std;

void input(int& n, int* (&original), int* (&origin_copy), int* (&target)) {
	cin >> n;

	original = new int[n];
	origin_copy = new int[n];
	target = new int[n];

	string o_temp, t_temp;
	cin >> o_temp >> t_temp;

	for (int i = 0; i < n; i++) {
		original[i] = o_temp[i] - '0';
		origin_copy[i] = original[i];
		target[i] = t_temp[i] - '0';
	}
	origin_copy[0] ^= 1, origin_copy[1] ^= 1;
}

bool compare_data(int n, int* (&a), int* (&b)) {
	for (int i = 0; i < n; i++) {
		if (a[i] != b[i])
			return false;
	}
	return true;
}

void change_state(int n, int idx, int* (&arr)) {
	for (int i = idx - 1; i < idx + 2; i++) {
		if (i < n)
			arr[i] ^= 1;
	}
}

int solution(int n, int* (&original), int* (&origin_copy), int* (target)) {
	int first = 0, second = 1;
	for (int i = 1; i < n; i++) {
		if (original[i - 1] != target[i - 1]) {
			change_state(n, i, original);
			first++;
		}

		if (origin_copy[i - 1] != target[i - 1]) {
			change_state(n, i, origin_copy);
			second++;
		}
	}

	first = (compare_data(n, original, target)) ? first : MAX;
	second = (compare_data(n, origin_copy, target)) ? second : MAX;

	return min(first, second);
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, answer = MAX;
	int *original, *origin_copy, *target;
	input(n, original, origin_copy, target);

	int result = solution(n, original, origin_copy, target);
	if (result == MAX)
		cout << "-1" << endl;
	else
		cout << result << endl;

	delete[] original;
	delete[] origin_copy;
	delete[] target;

	return 0;
}