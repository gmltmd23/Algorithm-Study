/*

백준 문제 2146번 그래프 탐색_다리 만들기

난이도가 꽤 높은 BFS 문제이다.
일단 다 풀지는 못했다. 내일이든 시간이 남을때 이어서 풀어야겠다.

접근법은 이렇게 하면 될거같다.
1. 대륙별 구분하기
2. 다리 연결하기

(2차커밋)
약간 더 진행해보았다.
각 대륙별로 다른 대륙에 닿을때까지 bfs를 돌려준다.
그리고 다른 대륙에 닿는 그 순간의 cost를 dist에 넣어준다.
그리고 최종적으로는 sort를 한뒤 최소값이면서 중복되는 값들의 개수를 세어주면 아마도 답이될거같다.

(최종커밋)
다리연결까지 완성하였다.
대륙의 개수를 세어주고, 그 수에 맞게끔 각각 bfs를 돌려주면 되는것이다.
처음에 짠 mkae_bridge 코드로는 85%에서 틀리다고 나와서
반례들을 찾아보니
5
1 0 0 0 0
1 0 0 0 1
1 1 1 0 1
0 0 0 0 0
0 0 0 1 0

이 경우에 답이 1이 나와야되는데 2가 나오는 경우가 있었다.
그 부분에 대한 예외처리를 적용해주었다.
그것은 예를들어 costs[i][j]에 3이 기록 됬는데,
다른 블록에서 온 값인 costs[now.first][now.second] + 1 값이 더 작을때
costs[i][j] = min(costs[i][j], costs[now.first][now.second] + 1)를 해주는 과정을 넣어줬다.
그러면 항상 최솟값들만 기록이 될것이다.

결국 답으로 리턴하는건 가장 최소값이니, 그것을 리턴해주면 정답이다.

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