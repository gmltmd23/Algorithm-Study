#include <iostream>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	priority_queue<long long> pq;
	int n, m, num;
	cin >> n >> m;

	while (n--) {
		cin >> num;
		pq.push(-num);
	}

	for (int i = 0; i < m; i++) {
		long long first = -pq.top();
		pq.pop();
		long long second = -pq.top();
		pq.pop();

		pq.push(-(first + second));
		pq.push(-(first + second));
	}

	long long answer = 0;
	while (!pq.empty()) {
		answer += -pq.top();
		pq.pop();
	}
	
	cout << answer << "\n";

	return 0;
}