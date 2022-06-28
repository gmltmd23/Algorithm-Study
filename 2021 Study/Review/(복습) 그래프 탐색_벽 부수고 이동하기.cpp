/*

(����) ���� ���� 2206�� �׷��� Ž��_�� �μ��� �̵��ϱ�

3���� �迭�� ����ؼ� ����üũ�� ������ߴ� �����̴�.
���� ������ ����� ������ ������ �ߵ��־ �״�� �ο��ϰڴ�.

����ó�� ����ϰ� ���� Ž���ϸ�, �� Element�� �湮�Ҷ����� �ʿ��� ����� �� Element�� ��ŷ�Ѵ�.
�׷��� �� ���������� ���࿡ ���� �����Ѵٸ� ������ DFS/BFS ����ó�� �װ��� �湮���ϴ°��� �ƴϰ�
�� 1���� ���� �������� �ִ�.

�� ���� ���� �� �ִ� ���¸� 3���� �迭�� �̿��Ͽ� visited�� ����д�.
�ɼ��̶�� �����ϸ� ���ҰŰ���. 0���ɼ��� ���� �ȸ�������, 1���ɼ��� ���� ������ 1���̶� ���� �վ�����
visited[x][y][0] = ���� �ѹ��� ������ �ʾ������� visited
visited[x][y][1] = ���� �ѹ� �վ������� visited

������ visited[x][y][0] ó�� 0�̾��� ���¿��ٰ� �ѹ��̶� �����հԵǸ�
�Լ��� ���������� visited[x][y][1] ó�� ���� �����������ִ� ���°� �� 1�� �ȴ�.

�ٽ� �����ڸ� ���� ���������� ����ϰ� ���� DFS/BFSó�� Ʈ��ŷ�ϴٰ�, ���� ������ �հ�
visited ���� �ɼ��� ��ȯ�Ǿ� ���� ���� visited �ʿ��� Ʈ��ŷ�� �ϴ°��̴�.

*/

#include<iostream>
#include<string>
#include<queue>

#define endl "\n"
#define MAX 1000
using namespace std;

int n, m;
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 };

int graph[MAX][MAX];
int visited[MAX][MAX][2];

struct Point
{
	int _x;
	int _y;
	int _wall;

	Point(int x, int y, int wall) : _x(x), _y(y), _wall(wall) {}
};

void input()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		string line;
		cin >> line;
		for (int j = 0; j < m; j++)
			graph[i][j] = line[j] - '0';
	}
}

int bfs()
{
	queue<Point> q;
	q.push(Point(0, 0, 0));
	visited[0][0][0] = 1;

	while (q.empty() == false)
	{
		Point now = q.front();
		q.pop();
		if (now._x == (n - 1) && now._y == (m - 1))
			return visited[now._x][now._y][now._wall];

		for (int i = 0; i < 4; i++)
		{
			int nx = now._x + dx[i];
			int ny = now._y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m && (visited[nx][ny][now._wall] == 0))
			{
				if (graph[nx][ny] == 0)
				{
					q.push(Point(nx, ny, now._wall));
					visited[nx][ny][now._wall] = visited[now._x][now._y][now._wall] + 1;
				}

				if (now._wall == 0 and graph[nx][ny] == 1)
				{
					q.push(Point(nx, ny, 1));
					visited[nx][ny][1] = visited[now._x][now._y][now._wall] + 1;
				}
			}
		}
	}

	return -1;
}

int main(void)
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	input();
	cout << bfs() << endl;

	return 0;
}