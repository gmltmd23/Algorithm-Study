/*

���� ���� 1448�� �׸���_�ﰢ�� �����

������ Ǯ�⿡ �ռ� �ﰢ���� ����� ������ �˾ƾ� �Ѵ�.
�ﰢ���� �̷�� �� ���� ���̸� �˰� �ִٰ� ����. (a, b, c �̷��� �� ��)
c�� ���� �� ���̶�� �� ��쿡 (c < (a + b))�� ������Ű�� �ﰢ���� ���������.

�� ������ ������Ű�� ���Ѵٸ� �ﰢ���� ���� �� ����.
���Ϳ� �°Բ� �ڵ带 ¥�ָ�ȴ�.

Ǫ�� ������μ��� sort�� �ؼ� ���� ū ������� ��Դ� ��� �Ǵ�,
���ʿ� ū���� ���� �����Բ� �켱����ť(heapq �ִ���)�� �ᵵ �ȴ�.

���� �ִ����� ����ؼ� Ǯ����.

*/

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int pop(priority_queue<unsigned int> &q) {
	unsigned int temp = q.top();
	q.pop();
	return temp;
}

int solution(priority_queue<unsigned int> q) {
	unsigned int c, b = pop(q), a = pop(q);
	while (!q.empty()) {
		c = b, b = a, a = pop(q);
		if (c < (a + b))
			return (a + b + c);
	}

	return -1;
}

int main() {
	int n;
	cin >> n;

	priority_queue<unsigned int> candidate;
	int temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		candidate.push(temp);
	}

	cout << solution(candidate) << endl;

	return 0;
}