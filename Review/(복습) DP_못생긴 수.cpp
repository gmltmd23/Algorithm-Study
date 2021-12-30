/*

(����) DP_������ ��

�̰��� �ڵ��׽�Ʈ�� å�� �ִ� �����̴�.
�ε����� �ϳ��� �������� DP�� �����ϴ� ��ũ���� �ʿ��� ��������.

*/

#include <iostream>
#include <fmt/ranges.h>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n;
	cin >> n;

	vector<int> ugly_numbers(n);
	ugly_numbers[0] = 1;

	int index_2 = 0, index_3 = 0, index_5 = 0;
	int two = 2, three = 3, five = 5;

	for (uint16_t i = 1; i < n; i++) {
		ugly_numbers[i] = min(two, (min(three, five)));
		if (ugly_numbers[i] == two)
			two = ugly_numbers[++index_2] * 2;
		if (ugly_numbers[i] == three)
			three = ugly_numbers[++index_3] * 3;
		if (ugly_numbers[i] == five)
			five = ugly_numbers[++index_5] * 5;
	}

	fmt::print("{}\n", ugly_numbers);

	return 0;
}