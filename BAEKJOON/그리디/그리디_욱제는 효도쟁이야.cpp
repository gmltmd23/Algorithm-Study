/*

백준 문제 14487 그리디_욱제는 효도쟁이야!!

간단한 그리디 문제인데..
문제설명이 진짜 이상하게 되어있다, 특히 '입력'에 대한 설명이 너무 이상하다.

어쨋든 이 문제의 본론은 모든 마을을 둥그렇게 둘러서 다 들릴건데,
최소비용을 말하라는것이다.

그러면 어떻게 하면 될까?
가장 큰 비용을 가진 길쪽으로 안가고 원형으로 돌면 되는것이다.

입력에 대한 설명중
둘째 줄에 i번째 마을과 i+1번째 마을의 이동비용 vi가 n개 주어진다. n번째 vi는 n번째 마을과 1번째 마을의 이동비용을 의미한다. (1 ≤ vi ≤ 1,000)
여기서 i번째 마을과 i + 1번째의 마을에 대한 정의가 명확하지가 않다.
그리고 n번째 vi는 n번째 마을과 1번째 마을의 이동비용을 의미한다라는데..
n이 1이라면 1번째 마을과 1번째 마을의 이동비용이 0보다 큰값으로 존재한다는 뜻이다.

설명이 너무 이상하게 되있던 문제였다.

*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	int total = 0, largest = 0;
	int now = 0;
	for (int i = 0; i < n; i++) {
		cin >> now;
		total += now;
		largest = max(largest, now);
	}

	cout << total - largest << endl;

	return 0;
}