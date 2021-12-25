/*

이것이 코딩테스트다 with python
(복습) 이분탐색_떡볶이 떡 만들기

이분탐색 문제이다.
떡볶이 떡을 어디를 썰어야 손님이 원하는 만큼의 양을 줄수있는지 맞추는 문제이다.
문제에서 주어진 n, m의 범위가 엄청 넓기 때문에,
범위만 보고도 이분탐색 문제인것을 눈치채줘야 한다.

예전에는 어렵게 풀었던거같은데 지금은 실력이 많이 늘긴했나보다.

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