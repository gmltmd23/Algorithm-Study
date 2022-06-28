/*

백준 문제 1504번 그래프 탐색_특정한 최단 경로

난이도가 업그레이드 된 다익스트라 문제이다.
특정 vertex 두 곳을 반드시 들려야 하는것으로 난이도를 올렸다.

이 문제의 요점은 2가지 이다.
1. 특정 vertex 두 곳을 반드시 들려야 한다.
2. e의 값은 0이 주어질수도 있다.

그러면 분기를 3가지로 나눌수가 있다.
1. e가 0으로 주어져서 아무것도 못하는 경우 => -1을 리턴해주자.
2. v1을 거치고 v2를 거쳐서 n으로 가는경우 => start[v1] + from_v1[v2] + from_v2[n]
3. v2를 거치고 v1를 거쳐서 n으로 가는경우 => start[v2] + from_v2[v1] + from_v1[n]
1번의 경우가 아닌이상 2번과 3번의 경우를 둘다 구하여 비교해서 최소값을 리턴해주면 된다.

*/

#include <iostream>
#include <vector>
#include <queue>

#define MAX_VALUE 987654321

using namespace std;

int n, e, v1, v2;
vector<vector<pair<int, int>>> graph;

void input() {
	cin >> n >> e;
	for (int i = 0; i < n + 1; i++)
		graph.push_back(vector<pair<int, int>>());

	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back(make_pair(b, c));
		graph[b].push_back(make_pair(a, c));
	}

	cin >> v1 >> v2;
}

int* dijkstra(int start) {
	priority_queue<pair<int, int>> pq;
	int* dist = new int[n + 1];
	for (int i = 1; i < n + 1; i++)
		dist[i] = MAX_VALUE;
	dist[start] = 0;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		int destination = pq.top().second;
		int value = -pq.top().first;
		pq.pop();

		if (dist[destination] < value)
			continue;
		for (pair<int, int> next : graph[destination]) {
			int new_value = value + next.second;
			if (new_value < dist[next.first]) {
				dist[next.first] = new_value;
				pq.push(make_pair(-dist[next.first], next.first));
			}
		}
	}

	return dist;
}

int solution() {
	if (e == 0) return -1;

	int* start = dijkstra(1);
	int* from_v1 = dijkstra(v1);
	int* from_v2 = dijkstra(v2);

	return min((start[v1] + from_v1[v2] + from_v2[n]), (start[v2] + from_v2[v1] + from_v1[n]));
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	input();
	cout << solution() << endl;

	return 0;
}