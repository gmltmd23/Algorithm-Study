/*

���� ���� 1520�� �׷��� Ž��_������ ��

DFS/BFS + DP �����̴�.
���̵��� ���� �����̴�.
�ϴ� dp�� ��������ʰ� DFS�� ���������쿡
�־��� ��� 4^(500 * 500)���� �۾��� �ʿ��ϱ� ������ �ð��ʰ��� �翬�� �߻��Ѵ�.

�׷��Ƿ� dp�� �̿��ؼ� �ʿ���°��� dfs�� �湮���� �ʵ��� ������ ������Ѵ�.
�׷��� ���ؼ� dp �׷����� ��� -1�� �ʱ�ȭ �Ͽ���.

-1�� �湮���� ������, -1�� �ƴѰ��� �ѹ��̶� �湮�ߴ����̴�.
�׷��� DP[x][y]���� -1�� �ƴѰ��� �ٷ� return DP[x][y]�� ���ؼ� �ð��� �������ִ� ���̴�.

�Ʒ� �ڵ��ζ�� DP������ ���̰� �𿩼� DP[0][0]�� ��ϵǰ� �ǹǷ�
���� DP[0][0]�� �ȴ�.

������ �ʿ��� �߿��� �����̴�.

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