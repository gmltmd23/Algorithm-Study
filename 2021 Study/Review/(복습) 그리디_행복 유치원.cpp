/*

���� ���� 13164�� �׸���_�ູ ��ġ��

���� ��� ¥�簣�� K���� ���� ����� �ű⼭ �ּ� ����� ������� �Ҹ��̴�.
�ϴ� ������ �ֵ鰣�� ���̸� ����ؼ� �����س��´�.
������� �� ���� 3 6 7 �̷��� ������ ������ ���̴� 3 1 �̴�.
�ٵ� �ᱹ �ʿ��Ѱ� �ִ�Ű�� �������� - �ּ�Ű�� �������� = 7 - 3 = 4 �ε�,
�׸��� 3 + 1 = 4 �� ����.

�׷� ��� �ǰڴ°�?
�Ʊ� ���س��� ������ ������������ ������ �ϸ� �����͵��� �տ����ϱ�
n - k����ŭ�� answer�� ���ʴ�� �����ָ� �����Եȴ�.

��������.

*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, k;
	cin >> n >> k;

	unsigned long* kids = new unsigned long[n];
	for (int i = 0; i < n; i++)
		cin >> kids[i];

	vector<unsigned long> diff;
	for (int i = 0; i < n - 1; i++)
		diff.push_back(kids[i + 1] - kids[i]);
	sort(diff.begin(), diff.end());

	int answer = 0;
	for (int i = 0; i < n - k; i++)
		answer += diff[i];

	cout << answer << endl;

	delete[] kids;
	return 0;
}