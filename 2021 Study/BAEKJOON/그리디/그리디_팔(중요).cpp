/*

백준 문제 1105번 그리디_팔

8의 개수를 찾는 문제이다.
수의 범위가 우선 엄청나게 크다 L, R이 될수있는 범위가 1 ~ 2,000,000,000 이므로
통상적인 브루트포스 방식으로 풀면 반드시 시간초과가 발생할것이다.

그렇다는것은 규칙을 찾아서 풀으라는 의미이다.
수를 굴리다보면 규칙이 보이긴한다.

예를들어 L = 12, R = 102 라고해보자.
답은 무조건 0이 나온다.
왜냐하면 자릿수가 다르게되면 무조건 그 자릿수가 다른 스타트의 숫자가 나오기때문에 8이 하나도 없는수가 나온다.
예를들어 8 15 라면 사이에 무조건 10이 있다.
99 100 이라면 사이에 100이 있다.
88 197 이라면 사이에 100이 있다.
127 37592 라면 사이에 1000도 있고, 10000도 있다.
즉 8이 한개도 안들어가는 수가 무조건 존재한다는것이다.

그럼 자릿수가 같을때를 보면될것이다.
8808 8880 을 보자.
이 둘의 사잇수는 8808, 8809, 8810, ..... 8877, 8878, 8879, 8880 이다.
여기서 절대 안바뀌는 숫자는 뭘까?

그렇다. 앞에 88 두개는 절대안바뀐다.
즉 최소 2개는 보장이 된다는 뜻이다.

또 다른 예를 보자.

80812 80899
여기서도 절대 안바뀌는 수는 첫번째 8과 세번째에 있는 8이다.
이를 이용해서 코드를 짜면된다.

*/

#include <iostream>
#include <string>

using namespace std;

long long L, R, diff;
string L_string, R_string;

void input() {
	cin >> L >> R;
	L_string = to_string(L);
	R_string = to_string(R);
}

int solution() {
	if (L_string.size() != R_string.size())
		return 0;

	int answer = 0;
	for (int i = 0; i < L_string.size(); i++) {
		if (L_string[i] == '8' && L_string[i] == R_string[i])
			answer++;
		else if (L_string[i] != R_string[i])
			break;
	}
	return answer;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	input();
	cout << solution() << endl;

	return 0;
}