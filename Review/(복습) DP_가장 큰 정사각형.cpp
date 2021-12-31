/*

���� ���� 1915�� DP_���� ū ���簢��

�̰� ������ �Ҷ��� Ǫ�� ����� ��� �������ϱ�,
DP���� �������� ������ ȿ���� �� �������� �����̴�.
���߿� ��޵ڿ� ���ȳ����� �ѹ� �� Ǯ��°� �����Ű���.

*/

#include <iostream>
#include <vector>

int n, m;

int main() {
	std::ios_base::sync_with_stdio(false); std::cin.tie(NULL); std::cout.tie(NULL);

	std::cin >> n >> m;
	std::vector<std::vector<int>> graph(n, std::vector<int>(m, 0));
	for (int i = 0; i < n; i++) {
		std::string line;
		std::cin >> line;
		for (int j = 0; j < m; j++)
			graph[i][j] = line[j] - 48;
	}

	std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));
	int answer = 0;
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < m + 1; j++) {
			if (graph[i - 1][j - 1] != 0) {
				dp[i][j] = std::min(dp[i - 1][j - 1], std::min(dp[i - 1][j], dp[i][j - 1])) + 1;
				answer = std::max(answer, dp[i][j]);
			}
		}
	}

	std::cout << answer * answer << "\n";

	return 0;
}