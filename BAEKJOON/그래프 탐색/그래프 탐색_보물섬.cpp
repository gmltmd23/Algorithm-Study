/*

백준 문제 2589번 그래프 탐색_보물섬

BFS문제이다.
처음에는 visited 배열을 두지않고, set 자료구조를 이용하여 방문체크를 하고,
answer를 전역변수로 두고 한 라운드가 돌때마다 time을 1씩 증가시키고 그것이 answer보다 크면
answer에 저장하는 방식으로 진행하였다.

이상하게도 정확도는 맞겠지만 시간초과가 계속 발생해서
방식을 바꾸게 되었다, 알고리즘을 크게 바꾼것도 없는데 왜 시간초과가 발생하는지 모르겠다.
set 자료구조를 사용하면 insert를 하거나, find를 할때에도 O(1)의 시간복잡도이므로 문제가 되지않을테고
answer를 전역변수로 써도 효율성에 영향이 가는 일은 없었을 것이다.

왜 안풀렸는지 모르겠다 기존코드로는

그래서 방법을 바꿨다. visited로 방문체크를 하는것 동시에
각 칸에 기록되는값이 answer보다 크면 answer에 기록되게 해주었다.

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