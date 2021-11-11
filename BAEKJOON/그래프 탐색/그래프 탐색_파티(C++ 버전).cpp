/*

���� ���� 1238�� �׷��� Ž��(�ִܰŸ�)_��Ƽ

���̽����� �ذ��� ������ C++�ε� Ǯ��Ҵ�.

���̽� �ڵ带 ���ֺ��ٰ� C++ �ڵ带 ���ϱ� ���� �������٤���������
�߰��� �ڵ� �ϳ� �Ǽ��ذ����� �ð� �� ��ƸԾ��µ� �׻� ��Ÿ�� ������..
������

*/

#include <iostream>
#include <vector>
#include <queue>
int INF = 1e9;

using namespace std;

struct edge {
	int node;
	int cost;

	edge(int node, int cost) {
		this->node = node;
		this->cost = cost;
	}

	bool operator<(const edge& e) const {
		return this->cost > e.cost;
	}
};

vector<int> dijkstra(vector<vector<edge>> &graph, int n, int start) {
	vector<int> distance(n + 1, INF);
	distance[start] = 0;

	priority_queue<edge> pq;
	pq.push(edge(start, 0));
	
	while (!pq.empty()) {
		edge temp = pq.top();
		pq.pop();
		
		if (!(distance[temp.node] < temp.cost)) {
			for (vector<edge>::iterator iter = graph[temp.node].begin(); iter != graph[temp.node].end(); iter++) {
				int cost = temp.cost + (*iter).cost;
				if (cost < distance[(*iter).node]) {
					distance[(*iter).node] = cost;
					pq.push(edge((*iter).node, cost));
				}
			}
		}
	}

	return distance;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, m, x;
	cin >> n >> m >> x;
	
	vector<vector<edge>> graph(n + 1, vector<edge>());
	int a, b, cost;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> cost;
		graph[a].push_back(edge(b, cost));
	}

	int answer = 0;
	vector<int> backward = dijkstra(graph, n, x);
	for (int i = 1; i < n + 1; i++) {
		if (i != x)
			answer = max(answer, dijkstra(graph, n, i)[x] + backward[i]);
	}
	cout << answer << "\n";

	return 0;
}