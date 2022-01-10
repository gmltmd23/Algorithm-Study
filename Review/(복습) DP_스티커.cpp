/*

(복습) 백준 문제 9465번 DP_스티커


저번 설명을 그대로 인용하겠다.

계속 보다보면 규칙은 보인다.
스티커를 찢으면 인접해있는 변을 가진 스티커들은 못 찢는다
이 말의 뜻은 대각선으로는 문제가 없다는 뜻이다.

즉 dp[0][i]가 최대값이 되려면 dp[1][i - 1]의 값을 저기에다가 더해줘야 한다.
그런데 예외가 있는 경우가 있다.
만약에 케이스가
50 10 100 20 40
30 50 70  10 60
이런 경우일때 50 -> 50 -> 100 -> 60 = 260을 선택하는게 가장 좋은 결과이다.
그런데 그냥 무작정 dp[0][i]는 dp[1][i - 1]을 더해주고
dp[1][0]는 dp[0][i - 1]를 더해주는 식으로 가게되면

50 -> 50 -> 100 -> 10 -> 40 = 250
30 -> 10 -> 70 -> 20 -> 60 = 190

우리가 원하는 260이라는 값이 안나오게 된다.
왜냐하면 마지막에서 100 -> 10 -> 40 을 해주는것보다, 100 -> 60 을 해주는것이 더 큰값이 나오기 때문이다.
그걸 이용하게 되면 점화식이 나오게 된다.

dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
*/

#include <iostream>

#define X 2

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int test_case;
	cin >> test_case;
	for (int t = 0; t < test_case; t++) {
		int Y;
		cin >> Y;

		int** dp;
		dp = new int*[X];
		for (int i = 0; i < X; i++) {
			dp[i] = new int[Y];
			for (int j = 0; j < Y; j++)
				cin >> dp[i][j];
		}

		dp[0][1] += dp[1][0];
		dp[1][1] += dp[0][0];
		for (int i = 2; i < Y; i++) {
			dp[0][i] += max(dp[1][i - 1], dp[1][i - 2]);
			dp[1][i] += max(dp[0][i - 1], dp[0][i - 2]);
		}
		cout << max(dp[0][Y - 1], dp[1][Y - 1]) << '\n';

		for (int i = 0; i < X; i++)
			delete[] dp[i];
		delete[] dp;
	}

	return 0;
}