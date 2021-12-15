/*

백준 문제 2146번 그래프 탐색_다리 만들기

난이도가 꽤 높은 BFS 문제이다.
일단 다 풀지는 못했다. 내일이든 시간이 남을때 이어서 풀어야겠다.

접근법은 이렇게 하면 될거같다.
1. 대륙별 구분하기
2. 다리 연결하기

대륙별 구분법은 그냥 bfs를 돌리면 쉽다. 번호를 매겨두던가 하자.
오늘은 대륙별 구분까지만 해놓았다.

(2차커밋)
약간 더 진행해보았다.
각 대륙별로 다른 대륙에 닿을때까지 bfs를 돌려준다.
그리고 다른 대륙에 닿는 그 순간의 cost를 dist에 넣어준다.
그리고 최종적으로는 sort를 한뒤 최소값이면서 중복되는 값들의 개수를 세어주면 아마도 답이될거같다.

위의 내용을 바탕으로 내일 해보자!

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