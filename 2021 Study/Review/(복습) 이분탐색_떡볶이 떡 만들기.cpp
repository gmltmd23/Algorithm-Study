/*

�̰��� �ڵ��׽�Ʈ�� with python
(����) �̺�Ž��_������ �� �����

�̺�Ž�� �����̴�.
������ ���� ��� ���� �մ��� ���ϴ� ��ŭ�� ���� �ټ��ִ��� ���ߴ� �����̴�.
�������� �־��� n, m�� ������ ��û �б� ������,
������ ���� �̺�Ž�� �����ΰ��� ��ġä��� �Ѵ�.

�������� ��ư� Ǯ�����Ű����� ������ �Ƿ��� ���� �ñ��߳�����.

*/

#include <fmt/format.h>
#include <iostream>
#include <vector>

int n, m;

int main() {
	std::ios_base::sync_with_stdio(false); std::cin.tie(NULL);
	std::cin >> n >> m;
	
	int start = 0, end = 0;
	std::vector<int> ddeoks(n);
	for (int i = 0; i < n; i++) {
		std::cin >> ddeoks[i];
		end = std::max(end, ddeoks[i]);
	}

	int mid = 0, total = 0;
	while (start < end) {
		mid = (start + end) / 2;
		total = 0;
		for (std::vector<int>::iterator iter = ddeoks.begin(); iter != ddeoks.end(); iter++) {
			if (*iter > mid)
				total += (*iter - mid);
		}

		if (total > m)
			start = mid;
		else if (total < m)
			end = mid;
		else
			break;
	}
	fmt::print("{}\n", mid);

	return 0;
}