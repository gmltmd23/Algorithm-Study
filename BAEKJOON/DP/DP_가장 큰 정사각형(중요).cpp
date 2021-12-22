/*

백준 문제 1915번 DP_가장 큰 정사각형

정답률 29%의 문제이다.
DP문제들이 대부분 어려우니깐뭐.. DP 문제들은 항상 아이디어를 떠올리는게 중요한거같다.
점화식을 만들어 내는것이 중요하다.

예를들어...
10
00
위 상태일 경우 가장 큰 정사각형의 넓이는 1이다.

11
11
위 상태의 경우 가장 큰 정사각형의 넓이는 4이다.

dp로 이것을 풀어나갈때 각 graph[i][j]의 요소가 1일때만 체크를 해주면된다.
graph[i][j]가 0이라면 애초에 정사각형이 이루어질수가 없으니깐 말이다.

점화식은 dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
이렇게 나온다.

잘 생각해보면 이렇다.
변의 길이가 2인 정사각형은
11
11
이렇게 생겼을것이고

변의 길이가 3인 정사각형은
111
111
111
이렇게 생겼을 것이다.

변의 길이가 3일때 dp로 나타내려면
111
121
113
이런식으로 만들어지게 된다.

정사각형을 만들때 오른쪽아래 꼭짓점이 기준이라고 하면,
그 기준을 바탕으로 왼쪽, 위, 왼쪽대각선은 항상 1로 채워져있을것이니깐 말이다.
그 원리를 이용해서 풀었다.

그림을 그려서 설명을 하면 금방 설명하는데
글로 설명하려니 잘 설명이 되지않는다ㅋㅋㅋㅋ

나중에 시간날때 복습도 하자.
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