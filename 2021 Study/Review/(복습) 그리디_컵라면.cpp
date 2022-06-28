/*

(����) ���� ���� 1781�� �׸���_�Ŷ��

�׸��� �����߿� ���� ������ �ϳ��̴�.
������� 30%����������, ������ �ϴ� ���� Ǯ����.

�켱����ť �ϳ��� �̿��ؼ� Ǯ���ִ� �����̱� �ϴٸ� C++ ���ΰ� �̰�����
stl�� �� �Ẹ�°� �����ϱ� vector�� ����, sort�� ���.

�� ��������.

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