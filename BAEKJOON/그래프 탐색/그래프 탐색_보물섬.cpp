/*

���� ���� 2589�� �׷��� Ž��_������

BFS�����̴�.
ó������ visited �迭�� �����ʰ�, set �ڷᱸ���� �̿��Ͽ� �湮üũ�� �ϰ�,
answer�� ���������� �ΰ� �� ���尡 �������� time�� 1�� ������Ű�� �װ��� answer���� ũ��
answer�� �����ϴ� ������� �����Ͽ���.

�̻��ϰԵ� ��Ȯ���� �°����� �ð��ʰ��� ��� �߻��ؼ�
����� �ٲٰ� �Ǿ���, �˰����� ũ�� �ٲ۰͵� ���µ� �� �ð��ʰ��� �߻��ϴ��� �𸣰ڴ�.
set �ڷᱸ���� ����ϸ� insert�� �ϰų�, find�� �Ҷ����� O(1)�� �ð����⵵�̹Ƿ� ������ ���������װ�
answer�� ���������� �ᵵ ȿ������ ������ ���� ���� ������ ���̴�.

�� ��Ǯ�ȴ��� �𸣰ڴ� �����ڵ�δ�

�׷��� ����� �ٲ��. visited�� �湮üũ�� �ϴ°� ���ÿ�
�� ĭ�� ��ϵǴ°��� answer���� ũ�� answer�� ��ϵǰ� ���־���.

*/

#include <iostream>
#include <queue>
#include <set>

#define MAX 50
using namespace std;

int x, y;
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 };

char graph[MAX][MAX];
int visited[MAX][MAX];

void input() {
	string line;
	for (int i = 0; i < x; i++) {
		cin >> line;
		for (int j = 0; j < y; j++)
			graph[i][j] = line[j];
	}
}

void reset() {
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			visited[i][j] = -1;
		}
	}
}

int bfs(int _x, int _y) {
	queue<pair<int, int>> q;
	q.push(make_pair(_x, _y));
	visited[_x][_y] = 0;

	int temp = 0;
	while (!q.empty()) {
		int bx = q.front().first;
		int by = q.front().second;
		q.pop();

		if (temp < visited[bx][by])
			temp = visited[bx][by];

		for (int i = 0; i < 4; i++) {
			int nx = (bx + dx[i]), ny = (by + dy[i]);
			if (0 <= nx && nx < x && 0 <= ny && ny < y) {
				if (visited[nx][ny] == -1 && graph[nx][ny] == 'L') {
					visited[nx][ny] = visited[bx][by] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}

	return temp;
}

int solution() {
	int answer = 0;

	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			if (graph[i][j] == 'L') {
				reset();
				answer = max(bfs(i, j), answer);
			}
		}
	}

	return answer;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> x >> y;
	input();
	cout << solution() << endl;

	return 0;
}