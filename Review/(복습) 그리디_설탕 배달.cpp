/*

(����) ���� ���� 2839�� �׸���_���� ���

����� 34%�� �׸��� �����̴�.
�������� Ǫ�°Ŷ� �׷��� �ٷ� Ǯ���� �ߴ�.

�� ������ �ܼ��ϴ�.
5�� ����������� answer���ٰ� (n / 5)�� Ȯ ���ؼ� �����ָ�ǰ�,
�׷��� �ʴٸ� ��� -3�� ���ָ鼭 ī������ ���ָ� �ȴ�.

������� n >= 0�� ���� �����Ͽ� �� ������ָ� ��

*/

#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	
	int answer = 0;
	while (n >= 0) {
		if (n % 5 == 0) {
			answer += (n / 5);
			break;
		}
		n -= 3;
		answer++;
	}

	if (n >= 0)
		cout << answer << '\n';
	else
		cout << -1 << '\n';

	return 0;
}