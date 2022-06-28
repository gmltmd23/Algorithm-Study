/*

(복습) 백준 문제 1781번 그리디_컵라면

그리디 문제중에 좋은 문제중 하나이다.
정답률은 30%정도이지만, 복습을 하니 쉽게 풀린다.

우선순위큐 하나만 이용해서 풀수있는 문제이긴 하다만 C++ 공부겸 이것저것
stl을 다 써보는게 좋으니깐 vector도 쓰고, sort도 썼다.

더 공부하자.

*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Problem {
	int deadline_;
	int cup_noodle_;

	Problem(int deadline, int cup_noodle) : deadline_(deadline), cup_noodle_(cup_noodle) {}

	bool operator<(const Problem& obj) const {
		return this->deadline_ < obj.deadline_;
	}
};

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	vector<Problem> pb;
	for (int i = 0; i < n; i++) {
		int deadline, cup_noodle;
		cin >> deadline >> cup_noodle;
		pb.push_back(Problem(deadline, cup_noodle));
	}
	sort(pb.begin(), pb.end());

	priority_queue<int> q;
	q.push(-pb[0].cup_noodle_);
	for (int i = 1; i < n; i++) {
		int deadline = pb[i].deadline_, cup_noodles = pb[i].cup_noodle_;
		q.push(-cup_noodles);
		if (q.size() > deadline)
			q.pop();
	}

	int answer = 0;
	while (!q.empty()) {
		answer += q.top();
		q.pop();
	}

	cout << -answer << endl;

	return 0;
}