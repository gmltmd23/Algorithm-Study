/*

백준 문제 12782번 그리디_비트 우정지수

아주 훌륭한 그리디문제이다.
공부할때는 이런걸 해야한다.
복습하기에 아주좋았다.

이 문제에서는 두가지의 연산을 사용할 수 있다.
1. 하나의 이진수에서 임의의 자리의 숫자를 0 또는 1로 바꾼다. (1번연산)
2. 하나의 이진수에서 서로 다른 자리에 있는 두 숫자의 위치를 바꾼다. (2번연산)

테스트 케이스마다 a, b 두개의 이진수 문자열을 받는다.
그때 a, b에 속한 1의 개수와 두 문자열에서 서로 다른 문자가 존재하는 경우를 카운팅 해준다.
(이때 1의 개수만 세어주는 이유는 어차피 2진수 이기때문에 1의 개수를 알면 0의 개수를 아는것과 같다. 0아니면 1밖에 없으니깐)

그리고 결과를 낼때는 2가지 경우로 나눠서 내주면 된다.

a의 1의개수, b의 1의개수 이 두가지로 차를 내서 절댓값을 낸다고 하면
만약 이게 0이라는건 "2번연산"은 했을수도 있지만 "1번연산"은 없는것을 알수가 있는것이고
만약 이게 0보다 크다면 "1번연산"을 했을 가능성이 생긴다.

그것을 이용해서 답을 내주면 된다.

*/

#include <iostream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main() {
	std::ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int t;
	cin >> t;

	int diff, a_one, b_one;
	while (t--) {
		string a, b;
		cin >> a >> b;

		diff = a_one = b_one = 0;
		for (int i = 0; i < a.size(); i++) {
			if (a[i] == '1')
				a_one++;

			if (b[i] == '1')
				b_one++;

			if (a[i] != b[i])
				diff++;
		}

		int result = 0, dist = abs(a_one - b_one);
		if (dist == 0)
			result += diff / 2;
		else
			result += ((diff - dist) / 2) + dist;

		cout << result << endl;
	}

	return 0;
}