/*

백준 문제 1052번 그리디_물병

처음에 이해하는데 난이도가 있는 문제였다.
가장 핵심인 이것을 이해하면 된다.

N == 13, K == 2일경우에 물병들을 합친다고 하는것은 2로 나누는것과 같다.
N / 2 = 6, N % 2 = 1 이라는 결과값이 나오는데
이말은 합쳐진것 6개, 못합쳐지고 남은것 1개라는 뜻이다.

계속 진행해보자,
합쳐진것 6개를 이용해서 또 합쳐본다.
6 / 2 = 3, 6 % 2 = 0
이말은 합쳐진것 3개, 못합쳐지고 남은것 0개라는 뜻이다.
아까 첫번째 과정에서 못합쳐지고 남은것 1개랑 방금나온 0개랑 더한다. (이것을 count라고 부르겠다. 그럼 count는 현재 1이다.)
그 다음 또 계속한다.

3 / 2 = 1, 3 % 2 = 1
이말은 합쳐진것 3개, 못합쳐지고 남은것 1개 (count = count + 1 = 2)

1 / 2 = 0, 1 % 2 = 1
이말은 합쳐진것 0개, 못합쳐지고 남은것 1개 (count = count + 1 = 3)

즉 count(모든과정을 끝내고 남은물병들의 개수)가 K보다 크다.
우리는 count의 수가 K이하 인것을 원한다.

그러기 위해서 상점에서 물병을 더 구입할 수 있다고 한다.
그럼 이제 N을 1 증가시키고 위의 과정을 계속해본다.
N == 14 였을때, N == 15 이 되더라도 count <= K를 만족시키지 못한다.

그런데 N == 16이 되는 순간 count <= K를 만족시킨다.
그러므로 답은 N(=16) - 처음주어진N(13) = 16 - 13 = 3이 될것이다.
근데 나는 answer을 따로 두어서 answer++로 그냥 답을 세주었다.

결과값을 내는것은 취향의 자유이다.

*/

#include <iostream>

using namespace std;

int solution(int n, int k) {
	if (n <= k)
		return 0;

	int answer = 0;
	while (true) {
		int temp = n, count = 0;
		while (temp > 0) {
			if (temp % 2 == 1)
				count++;
			temp /= 2;
		}

		if (count <= k)
			return answer;

		answer++;
		n++;
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n, k;
	cin >> n >> k;

	cout << solution(n, k) << endl;

	return 0;
}