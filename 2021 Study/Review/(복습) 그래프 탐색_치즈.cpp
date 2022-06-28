/*

백준 문제 2636 그래프 탐색_치즈

테두리는 갈수없다는것을 이용해서 풀면 되는 BFS문제이다.
처음 풀었을때는 뭔가 잘안풀렸었던 문제였었다.

*/

#include <iostream>
#include <queue>

#define MAX 100
using namespace std;

int graph[MAX][MAX];
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 };
int total = 0;
int n, m;

void input() {
	cin >> n >> m;
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < m; y++) {
			cin >> graph[x][y];
			if (graph[x][y] == 1)
				total += 1;
		}
	}
}

void bfs() {
	vector<vector<bool>> visited(n, vector<bool>(m, false));
	visited[0][0] = true;

	queue<pair<int, int>> q;
	q.push(make_pair(0, 0));

	while (!q.empty()) {
		auto now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = now.first + dx[i];
			int ny = now.second + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (!visited[nx][ny]) {
					visited[nx][ny] = true;
					if (graph[nx][ny] == 1) {
						graph[nx][ny] = 0;
						total--;
					}
					else
						q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

int main() {
	input();

	int before, round = 0;
	while (total != 0) {
		before = total;
		bfs();
		round++;
	}

	cout << round << '\n' << before << '\n';

	return 0;
}