/*

���� ���� 1504�� �׷��� Ž��_Ư���� �ִ� ���

���̵��� ���׷��̵� �� ���ͽ�Ʈ�� �����̴�.
Ư�� vertex �� ���� �ݵ�� ����� �ϴ°����� ���̵��� �÷ȴ�.

�� ������ ������ 2���� �̴�.
1. Ư�� vertex �� ���� �ݵ�� ����� �Ѵ�.
2. e�� ���� 0�� �־������� �ִ�.

�׷��� �б⸦ 3������ �������� �ִ�.
1. e�� 0���� �־����� �ƹ��͵� ���ϴ� ��� => -1�� ����������.
2. v1�� ��ġ�� v2�� ���ļ� n���� ���°�� => start[v1] + from_v1[v2] + from_v2[n]
3. v2�� ��ġ�� v1�� ���ļ� n���� ���°�� => start[v2] + from_v2[v1] + from_v1[n]
1���� ��찡 �ƴ��̻� 2���� 3���� ��츦 �Ѵ� ���Ͽ� ���ؼ� �ּҰ��� �������ָ� �ȴ�.

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