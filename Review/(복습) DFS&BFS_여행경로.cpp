/*

(복습) 프로그래머스 LEVEL 3 : 여행경로

DFS문제이다.
여러가지 풀었었던 DFS/BFS문제중 어려운 문제는 아니다만
그래도 stack에 들어가는 값들을 신경쓰면서 풀어야 했었던 문제이다.

복습하면서 확실히 느끼는건데 알고리즘 실력이 많이 좋아졌다.
앞으로도 정진하자ㅋㅋㅋ

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