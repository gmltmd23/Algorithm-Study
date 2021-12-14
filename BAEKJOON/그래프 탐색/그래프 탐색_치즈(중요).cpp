/*

백준 문제 2636 그래프 탐색_치즈

원래같았으면 금방 푸는 문제였는데, 오늘 머리가 복잡해서 그런지
잘 풀리지가 않았다. 그래서 오래걸림..

문제를 푸는법은 bfs로 풀면되는데
무조건 (0, 0)에서 탐색을 시작한다고 생각하면 된다.
문제 설명 상 테두리를 두르고있는곳은 침범할수없는 영역이기에 그것을 이용해서 문제를 푸는것이다.

매 라운드마다 (0, 0)에서 bfs를 시작해주면 항상 치즈 내부영역을 제외한 바깥영역만 탐색할수있다.
그러면 탐색을 돌면서 graph 상에서 1을 만나면 0으로 바꿔주기만 하면 된다.

복습하기에 좋은 문제이다.

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