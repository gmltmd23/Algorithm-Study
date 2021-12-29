/*

(����) ���� ���� 2146�� �׷��� Ž��_�ٸ� �����

ó���� Ǯ���� �� �����ð��� �ɷ��� Ǯ������ �����̴�.
���� ������ �Ӹ��� ����� �����־ �ݹ� Ǯ���� �־��ٰ�� �ص�,
DFS/BFS �����鵵 Ȯ���� ������ ���� ���̵��� ��������
������ �����ص־� �Ѵ�.

����������.

*/

#include <iostream>
#include <queue>
#include <vector>

#define MAX 100
#define endl '\n'
using namespace std;

int n;
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 }; // LRUD
int graph[MAX][MAX], visited[MAX][MAX] = { false };

void input();
void clear_visited();
int first_step();
void make_territory(int, int, int);
void second_step(const int);
void make_bridge(int, int, int, vector<vector<int>>&);

int answer = 1e9;

int main() {
	input();

	int territory_count = first_step();
	second_step(territory_count);

	if (answer == 1e9)
		cout << 0 << endl;
	else
		cout << answer << endl;

	return 0;
}

void input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cin >> graph[i][j];
	}
}

int first_step() {
	int number = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j] && graph[i][j] == 1)
				make_territory(i, j, number++);
		}
	}
	return (number - 1);
}

void make_territory(int x, int y, int number) {
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	visited[x][y] = true;
	graph[x][y] = number;

	while (!q.empty()) {
		auto now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = now.first + dx[i];
			int ny = now.second + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < n) {
				if (!visited[nx][ny] && graph[nx][ny] == 1) {
					visited[nx][ny] = true;
					graph[nx][ny] = number;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

void second_step(const int territory_count) {
	for (int count = 1; count <= territory_count; count++) {
		vector<vector<int>> costs(n, vector<int>(n, -1));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (costs[i][j] == -1 && graph[i][j] == count) {
					make_bridge(i, j, count, costs);
				}
			}
		}
	}
}

void make_bridge(int x, int y, int number, vector<vector<int>>& costs) {
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	costs[x][y] = 0;

	while (!q.empty()) {
		auto now = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = now.first + dx[i];
			int ny = now.second + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < n) {
				if (costs[nx][ny] == -1) {
					if (graph[nx][ny] == number) {
						costs[nx][ny] = 0;
						q.push(make_pair(nx, ny));
					}
					else if (graph[nx][ny] == 0) {
						costs[nx][ny] = costs[now.first][now.second] + 1;
						q.push(make_pair(nx, ny));
					}
					else
						answer = min(answer, costs[now.first][now.second]);
				}
				else if (costs[nx][ny] != -1 && costs[nx][ny] != 0)
					costs[nx][ny] = min(costs[nx][ny], costs[now.first][now.second] + 1);
			}
		}
	}
}