/*

백준 문제 5545번 그리디_최고의 피자

백준에서 '다국어' 라고 써있는 문제들은 한글로 좀 이상하게 쓰여있는거같다.
대개 이런 문제들이 그렇지만 보통 푸는 방법은 두 가지이다.

정렬을 통해서 풀거나, 우선순위큐(heapq)를 이용해서 풀거나.
정렬을 이용해서 풀면 보통 시간복잡도는 O(n + n*log n + n) = O(n*log n) 정도 나온다. [초기화 + sort + 답 구하기]
힙구조를 이용해서 풀면 시간복잡도는 O(n*log n + n*log n) = O(n*log n) 정도 나온다.
결국에는 같다.

더 복잡하게 따지자면 이 문제 같은 경우에는 sort쪽이 메모리는 힙보다는 덜쓰니깐 조금 더 좋은정도..?
뭘 쓰든 문제를 푸는사람의 취향차이이다.

나는 sort로 풀어봤다.

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