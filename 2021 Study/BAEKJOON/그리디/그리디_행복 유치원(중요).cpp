/*

백준 문제 13164번 그리디_행복 유치원

조를 어떻게 짜든간에 K개의 조를 만들고 거기서 최소 비용을 뽑으라는 소리이다.
일단 인접한 애들간의 차이를 계산해서 저장해놓는다.
예를들어 한 조에 3 6 7 이렇게 세명이 있으면 차이는 3 1 이다.
근데 결국 필요한건 최대키를 가진아이 - 최소키를 가진아이 = 7 - 3 = 4 인데,
그말은 3 + 1 = 4 와 같다.

그럼 어떻게 되겠는가?
아까 구해놓은 차들을 오름차순으로 정렬을 하면 작은것들이 앞에가니깐
n - k번만큼만 answer에 차례대로 더해주면 끝나게된다.

복습하자.

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