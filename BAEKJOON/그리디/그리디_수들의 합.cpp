/*

���� ���� 1789�� �׸���_������ ��

�������� ���� �ٸ� N���� �ڿ����� ���� S��� �Ұ�쿡
N�� �ִ��� ���϶�µ� �̷���쿡�� 
1���� �������� ���� S�� �ɶ����� �����ָ� �ȴ�.

����������� ���ؾ� ���� �ٸ� N���� ������ �������״� ���̴�.
���� ������ �ణ �ν������� ���Ҵ� �����̴�.

*/

#include <iostream>

using namespace std;
unsigned long long N, S;

int main() {
	cin >> S;
	unsigned long long total = 0;
	int result = 0;
	for (N = 1; N < S; N++) {
		total += N;
		if (total > S)
			break;
		result++;
	}

	cout << result << endl;

	return 0;
}