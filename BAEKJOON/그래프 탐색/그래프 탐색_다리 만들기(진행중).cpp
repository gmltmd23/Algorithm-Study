/*

���� ���� 2146�� �׷��� Ž��_�ٸ� �����

���̵��� �� ���� BFS �����̴�.
�ϴ� �� Ǯ���� ���ߴ�. �����̵� �ð��� ������ �̾ Ǯ��߰ڴ�.

���ٹ��� �̷��� �ϸ� �ɰŰ���.
1. ����� �����ϱ�
2. �ٸ� �����ϱ�

����� ���й��� �׳� bfs�� ������ ����. ��ȣ�� �Űܵδ��� ����.
������ ����� ���б����� �س��Ҵ�.

(2��Ŀ��)
�ణ �� �����غ��Ҵ�.
�� ������� �ٸ� ����� ���������� bfs�� �����ش�.
�׸��� �ٸ� ����� ��� �� ������ cost�� dist�� �־��ش�.
�׸��� ���������δ� sort�� �ѵ� �ּҰ��̸鼭 �ߺ��Ǵ� ������ ������ �����ָ� �Ƹ��� ���̵ɰŰ���.

���� ������ �������� ���� �غ���!

*/

#include <iostream>
#include <queue>
#include <list>

#define MAX 100
#define endl '\n'
using namespace std;

int n;
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 }; // LRUD
int graph[MAX][MAX], visited[MAX][MAX] = { false };
list<int> dist;

void input();

int first_step();
void make_territory(int, int, int);
void second_step();

int main() {
	input();

	int territory_count = first_step();

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
	return number;
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

void second_step() {

}