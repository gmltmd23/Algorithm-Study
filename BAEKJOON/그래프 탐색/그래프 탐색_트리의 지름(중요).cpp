/*

백준 문제 1967번 그래프 탐색_트리의 지름

난이도를 올린 DFS문제였다.
사람들이 DFS/BFS 문제를 풀때 언제 DFS를 써야되는지 BFS를 써야되는지 헷갈리는 경우가있다.
나도 알고리즘 문제들을 꽤 오래풀다보니 이제 그냥 감이와서 뭘써야되는지 알긴아는데
대충 정리해보면, DFS는 이 문제와 같이 트리를 다루거나 먼저 처음부터 끝까지 가서 결과를 찍고와야되는 경우들이 그렇다.
그와 반대로 BFS는 DFS와 다르게 모든 경우의수를 동등한 속도로 같이 밀고갈수있다.

쉽게 얘기하자면 DFS는 경로탐색 도중 결과를 저장하면서 가져가야할때 사용하고
BFS는 그렇지않을때 사용한다.
어차피 DFS, BFS 둘다 모든 노드를 탐색하는 알고리즘이기에 기본적으로 시간복잡도는 (V = vertex, E = edge)
인접행렬로 구현할 경우에 O(V^2)이고 인접리스트일경우 O(V + E) 만큼 걸린다.

갑자기 이야기가 다른곳으로 가버렸다.
이제 문제를 보자.

트리의 지름을 구하는 문제이다.
말이 지름이지 걍 노드 <-> 노드 이렇게 왔다갔다 할때 cost가 최대가 되는 값을 말하라는것이다.
DFS를 써서 푸는데 최적인 문제이다.

처음 풀었을때는 각 노드마다 indegree수를 측정하여 리프노드들을 찾고,
리프노드에서 리프노드까지 걸리는 cost중 최대가 되는것을 리턴했더니 시간초과로 문제를 풀수가 없었다.
노드의 개수가 최대 10000개니깐 리프노드가 9999개가 되는경우를 생각해보면
걸리는 시간이 O(v^2)이므로 당연히 시간초과가 날것이다.

그러면 이것을 빠르게 푸는 아이디어가 필요하다는 것이다.
그 아이디어는 굳이 리프노드를 찾을 필요가 없이, 어느 한 노드 A에서 DFS를 돌리면
결국 최대 cost가 필요한 어느 한 노드 B에 도달하게 될것이다.

그렇게 되면 그 노드 B에서 다시 DFS를 돌리고,
거기에서 최대 cost가 필요한 어느 한 노드 C에 도달하게 될때의 cost가 정답이 된다.

왜그럴까??
문제에 있는 그림을 봐도 알겠지만, 노드 2개를 잇는 가장 긴 지름을 형성하게 된다면
나머지 노드들은 원 안에 위치하게 된다.
그러면 임의의 나머지 노드A에서 가장 멀리 도달하게 되는 노드B는
지름을 형성하고 있는 노드중 가장 멀리있는(cost가 가장 많이필요한) 노드가 된다.

그러면 이제 노드B에서 dfs를 돌리고 cost가 가장 많이 드는 노드C를 찾으면
B와 같이 지름을 이루고 있던 노드 C를 찾은것이다.
그때 발생하는 cost가 이 문제의 답이되는것이고..
좋은 문제였다. 나중에 복습해도 좋을거같다.

*/

#include <iostream>
#include <vector>
#include <unordered_set>
#include <stack>

using namespace std;

int n;
vector<pair<int, int>> tree[10001];

void input() {
	cin >> n;

	int a, b, c;
	for (int i = 0; i < n - 1; i++) {
		cin >> a >> b >> c;
		tree[a].push_back(make_pair(b, c));
		tree[b].push_back(make_pair(a, c));
	}
}

pair<int, int> dfs(int start) {
	unordered_set<int> visited;
	visited.insert(start);
	stack<pair<int, int>> stk;
	stk.push(make_pair(start, 0));

	int answer = 0;
	int destination = 0;
	while (!stk.empty()) {
		pair<int, int> now = stk.top();
		stk.pop();

		for (pair<int, int> next : tree[now.first]) {
			if (visited.find(next.first) == visited.end()) {
				visited.insert(next.first);
				int next_cost = now.second + next.second;
				stk.push(make_pair(next.first, next_cost));
				if (answer < next_cost) {
					answer = next_cost;
					destination = next.first;
				}
			}
		}
	}

	return make_pair(answer, destination);
}

int main() {
	input();

	auto temp = dfs(1);
	auto answer = dfs(temp.second);
	cout << answer.first << endl;
	
	return 0;
}