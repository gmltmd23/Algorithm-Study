#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, deadline, score;
	cin >> n;

	vector<pair<int, int>> assignments;
	for (int i = 0; i < n; i++) {
		cin >> deadline >> score;
		assignments.push_back({ deadline, score });
	}
	sort(assignments.begin(), assignments.end());

	priority_queue<int> pq;
	for (auto iter = assignments.begin(); iter != assignments.end(); iter++) {
		pair<int, int> temp = *iter;
		pq.push(-temp.second);
		if (pq.size() > temp.first)
			pq.pop();
	}
	
	int answer = 0;
	while (!pq.empty()) {
		answer += -pq.top();
		pq.pop();
	}

	cout << answer << "\n";

	return 0;
}