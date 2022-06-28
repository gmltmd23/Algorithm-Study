/*

���� ���� 1967�� �׷��� Ž��_Ʈ���� ����

���̵��� �ø� DFS��������.
������� DFS/BFS ������ Ǯ�� ���� DFS�� ��ߵǴ��� BFS�� ��ߵǴ��� �򰥸��� ��찡�ִ�.
���� �˰��� �������� �� ����Ǯ�ٺ��� ���� �׳� ���̿ͼ� ����ߵǴ��� �˱�ƴµ�
���� �����غ���, DFS�� �� ������ ���� Ʈ���� �ٷ�ų� ���� ó������ ������ ���� ����� ���;ߵǴ� ������ �׷���.
�׿� �ݴ�� BFS�� DFS�� �ٸ��� ��� ����Ǽ��� ������ �ӵ��� ���� �а����ִ�.

���� ������ڸ� DFS�� ���Ž�� ���� ����� �����ϸ鼭 ���������Ҷ� ����ϰ�
BFS�� �׷��������� ����Ѵ�.
������ DFS, BFS �Ѵ� ��� ��带 Ž���ϴ� �˰����̱⿡ �⺻������ �ð����⵵�� (V = vertex, E = edge)
������ķ� ������ ��쿡 O(V^2)�̰� ��������Ʈ�ϰ�� O(V + E) ��ŭ �ɸ���.

���ڱ� �̾߱Ⱑ �ٸ������� �����ȴ�.
���� ������ ����.

Ʈ���� ������ ���ϴ� �����̴�.
���� �������� �� ��� <-> ��� �̷��� �Դٰ��� �Ҷ� cost�� �ִ밡 �Ǵ� ���� ���϶�°��̴�.
DFS�� �Ἥ Ǫ�µ� ������ �����̴�.

ó�� Ǯ�������� �� ��帶�� indegree���� �����Ͽ� ���������� ã��,
������忡�� ���������� �ɸ��� cost�� �ִ밡 �Ǵ°��� �����ߴ��� �ð��ʰ��� ������ Ǯ���� ������.
����� ������ �ִ� 10000���ϱ� ������尡 9999���� �Ǵ°�츦 �����غ���
�ɸ��� �ð��� O(v^2)�̹Ƿ� �翬�� �ð��ʰ��� �����̴�.

�׷��� �̰��� ������ Ǫ�� ���̵� �ʿ��ϴٴ� ���̴�.
�� ���̵��� ���� ������带 ã�� �ʿ䰡 ����, ��� �� ��� A���� DFS�� ������
�ᱹ �ִ� cost�� �ʿ��� ��� �� ��� B�� �����ϰ� �ɰ��̴�.

�׷��� �Ǹ� �� ��� B���� �ٽ� DFS�� ������,
�ű⿡�� �ִ� cost�� �ʿ��� ��� �� ��� C�� �����ϰ� �ɶ��� cost�� ������ �ȴ�.

�ֱ׷���??
������ �ִ� �׸��� ���� �˰�����, ��� 2���� �մ� ���� �� ������ �����ϰ� �ȴٸ�
������ ������ �� �ȿ� ��ġ�ϰ� �ȴ�.
�׷��� ������ ������ ���A���� ���� �ָ� �����ϰ� �Ǵ� ���B��
������ �����ϰ� �ִ� ����� ���� �ָ��ִ�(cost�� ���� �����ʿ���) ��尡 �ȴ�.

�׷��� ���� ���B���� dfs�� ������ cost�� ���� ���� ��� ���C�� ã����
B�� ���� ������ �̷�� �ִ� ��� C�� ã�����̴�.
�׶� �߻��ϴ� cost�� �� ������ ���̵Ǵ°��̰�..
���� ��������. ���߿� �����ص� �����Ű���.

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