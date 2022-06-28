/*

(복습) 백준 문제 1520번 그래프 탐색_내리막 길

이 문제는 DFS + DP 문제이다.
일반적인 DFS 방식으로만 접근하면 시간복잡도가 거의 500^500 급으로 커져서 답도없다.
DP 방식을 적용하여, 맵에다가 기록을 하면서 가야한다.
방문할 필요성이 없는곳은 방문하지 않는 방식으로 바꿔주면 가능하다.

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