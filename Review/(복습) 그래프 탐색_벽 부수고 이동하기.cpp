/*

(복습) 백준 문제 2206번 그래프 탐색_벽 부수고 이동하기

3차원 배열을 사용해서 상태체크를 해줘야했던 문제이다.
내가 기존에 써놨던 설명문이 설명이 잘되있어서 그대로 인용하겠다.

기존처럼 평범하게 맵을 탐색하며, 각 Element를 방문할때마다 필요한 비용을 그 Element에 마킹한다.
그런데 이 문제에서는 만약에 벽이 존재한다면 기존의 DFS/BFS 문제처럼 그곳을 방문안하는것이 아니고
딱 1번만 벽을 뚫을수가 있다.

그 벽을 뚫을 수 있는 상태를 3차원 배열을 이용하여 visited에 적어둔다.
옵션이라고 생각하면 편할거같다. 0번옵션은 벽을 안만났을때, 1번옵션은 벽을 만나서 1번이라도 벽을 뚫었을때
visited[x][y][0] = 벽을 한번도 만나지 않았을때의 visited
visited[x][y][1] = 벽을 한번 뚫었을때의 visited

원래는 visited[x][y][0] 처럼 0이었던 상태였다가 한번이라도 벽을뚫게되면
함수가 끝날때까지 visited[x][y][1] 처럼 끝에 벽을뚫을수있는 상태가 쭉 1로 된다.

다시 말하자면 벽을 만나기전에 평범하게 기존 DFS/BFS처럼 트래킹하다가, 벽을 만나면 뚫고
visited 맵의 옵션이 전환되어 벽을 뚫은 visited 맵에서 트래킹을 하는것이다.

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