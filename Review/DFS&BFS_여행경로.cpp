/*

(����) ���α׷��ӽ� LEVEL 3 : ������

DFS�����̴�.
�������� Ǯ������ DFS/BFS������ ����� ������ �ƴϴٸ�
�׷��� stack�� ���� ������ �Ű澲�鼭 Ǯ��� �߾��� �����̴�.

�����ϸ鼭 Ȯ���� �����°ǵ� �˰��� �Ƿ��� ���� ��������.
�����ε� �������ڤ�����

*/

#include <iostream>
#include <unordered_map>
#include <stack>
#include <queue>
#include <algorithm>
#include <fmt/ranges.h>

using namespace std;
using pq = priority_queue<string, vector<string>, greater<string>>;

void dfs(vector<string> &answer, unordered_map<string, pq> &dict) {
	stack<string> st;
	st.push("ICN");

	while (!st.empty()) {
		auto now = st.top();
		if (dict.find(now) != dict.end() && !dict[now].empty()) {
			st.push(dict[now].top());
			dict[now].pop();
		}
		else {
			answer.push_back(st.top());
			st.pop();
		}
	}
}

vector<string> solution(vector<vector<string>> tickets) {
	unordered_map<string, pq> dict;
	for (vector<string> element : tickets) {
		if (dict.find(element[0]) == dict.end())
			dict[element[0]] = pq();
		dict[element[0]].push(element[1]);
	}

	vector<string> answer;
	dfs(answer, dict);
	reverse(answer.begin(), answer.end());
	return answer;
}

int main() {
	vector<vector<string>> tickets;
	tickets.push_back(vector<string>{"ICN", "SFO"});
	tickets.push_back(vector<string>{"ICN", "ATL"});
	tickets.push_back(vector<string>{"SFO", "ATL"});
	tickets.push_back(vector<string>{"ATL", "ICN"});
	tickets.push_back(vector<string>{"ATL", "SFO"});

	fmt::print("{}\n", solution(tickets));
	return 0;
}