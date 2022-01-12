/*

(복습) 자료구조_가운데를 말해요

우선순위큐를 2개 사용해야 풀수있는 문제이다.
난이도가 있던 문제였는데, 이런게 실력을 향상시키기 적절한 문제라고 생각한다.

*/

#include <iostream>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	priority_queue<int> left_heap, right_heap;
	for (int _ = 0; _ < n; _++) {
		int number;
		cin >> number;
		if (left_heap.size() == right_heap.size())
			left_heap.push(number);
		else
			right_heap.push(-number);

		if (!(right_heap.empty()) && left_heap.top() > -right_heap.top()) {
			int left_value = left_heap.top();
			left_heap.pop();
			int right_value = -right_heap.top();
			right_heap.pop();

			left_heap.push(right_value);
			right_heap.push(-left_value);
		}

		cout << left_heap.top() << "\n";
	}

	return 0;
}