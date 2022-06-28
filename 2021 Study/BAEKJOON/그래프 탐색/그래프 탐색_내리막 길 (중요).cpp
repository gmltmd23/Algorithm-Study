/*

백준 문제 1520번 그래프 탐색_내리막 길

DFS/BFS + DP 문제이다.
난이도가 높은 수준이다.
일단 dp를 사용하지않고 DFS만 사용했을경우에
최악의 경우 4^(500 * 500)번의 작업이 필요하기 때문에 시간초과가 당연히 발생한다.

그러므로 dp를 이용해서 필요없는곳은 dfs가 방문하지 않도록 설정을 해줘야한다.
그러기 위해서 dp 그래프를 모두 -1로 초기화 하였다.

-1은 방문하지 않은곳, -1이 아닌곳은 한번이라도 방문했던곳이다.
그래서 DP[x][y]값이 -1이 아닌곳은 바로 return DP[x][y]를 통해서 시간을 절약해주는 것이다.

아래 코드대로라면 DP값들이 모이고 모여서 DP[0][0]에 기록되게 되므로
답은 DP[0][0]이 된다.

복습이 필요한 중요한 문제이다.

*/

#include <iostream>
#include <vector>

#define endl "\n"
#define MAX 500

using namespace std;

int n, m;
int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };

int graph[MAX][MAX];
int DP[MAX][MAX];

int dfs(int x, int y) {
	if (x == n - 1 && y == m - 1) return 1;
	if (DP[x][y] != -1) return DP[x][y];

	DP[x][y] = 0;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < n && 0 <= ny && ny < m) {
			if (graph[nx][ny] < graph[x][y]) {
				DP[x][y] = DP[x][y] + dfs(nx, ny);
			}
		}
	}

	return DP[x][y];
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> graph[i][j];
			DP[i][j] = -1;
		}
	}
	cout << dfs(0,0) << endl;
}