/*

���� ���� 5545�� �׸���_�ְ��� ����

���ؿ��� '�ٱ���' ��� ���ִ� �������� �ѱ۷� �� �̻��ϰ� �����ִ°Ű���.
�밳 �̷� �������� �׷����� ���� Ǫ�� ����� �� �����̴�.

������ ���ؼ� Ǯ�ų�, �켱����ť(heapq)�� �̿��ؼ� Ǯ�ų�.
������ �̿��ؼ� Ǯ�� ���� �ð����⵵�� O(n + n*log n + n) = O(n*log n) ���� ���´�. [�ʱ�ȭ + sort + �� ���ϱ�]
�������� �̿��ؼ� Ǯ�� �ð����⵵�� O(n*log n + n*log n) = O(n*log n) ���� ���´�.
�ᱹ���� ����.

�� �����ϰ� �����ڸ� �� ���� ���� ��쿡�� sort���� �޸𸮴� �����ٴ� �����ϱ� ���� �� ��������..?
�� ���� ������ Ǫ�»���� ���������̴�.

���� sort�� Ǯ��ô�.

*/

#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int n, a, b, dough_kcal;
list<int> topings_kcal;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n >> a >> b >> dough_kcal;
	for (int i = 0; i < n; i++) {
		int toping;
		cin >> toping;
		topings_kcal.push_back(toping);
	}
	topings_kcal.sort(greater<int>());

	int answer = dough_kcal / a;
	int toping_total = 0, count = 1;
	for (list<int>::iterator iter = topings_kcal.begin(); iter != topings_kcal.end(); iter++) {
		toping_total += *iter;
		answer = max(answer, (dough_kcal + toping_total) / (a + (count++ * b)));
	}

	cout << answer << endl;

	return 0;
}