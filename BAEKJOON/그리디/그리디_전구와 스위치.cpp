/*

���� ���� 2138�� �׸���_������ ����ġ

������ ���̵��� ���� ���� �׸��� �����̴�.
�ʹݿ� ������ ���������ʾƼ� �����ʸ� ���ͳ��� �����Ͽ���.

�ڵ带 �� �������� ����, �ٸ��е��� �ڵ�� ���������°� ����.
���� ���������� string�� int�� �迭�� �ٲٰ� ON/OFF�� XOR�� �����ϴ°��� ���� �װɷ��ߴٸ�,
string�� int�迭�� �ٲܶ� O(n)��ŭ�� �ð��� ����ϹǷ� ������ �ð��̶� ���̰� ��������� string �״�� ����ϴ°� ���ٰ���.
�ٵ� XOR���� ���� ����������..

������ �ٽ��� �̰Ŵ�.
i��° ����ġ�� ������ i-1, i, i+1 ��° ������ ������ ����.
������� ���ϱ��� �迭�� i��° ���Ұ� ��ǥ�� �ϴ� target[i]�� ���ٸ� �װ� �ٲ��ʿ䰡 ��������
�ٸ��ٸ� �ٲ�����Ѵ�. �׷��� i-1��°�� �ٲٷ��� i��° ����ġ�� ������ȴ�. �װ� ���� �����̴ϱ�.

�̷��� ��찡 ������.
0��° ����ġ�� �������, �ȴ������
�� �ΰ��� ��츦 ������ ó������ ������ �������شٸ� ������ Ǯ����.
���߿� ��������.

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