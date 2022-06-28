/*

백준 문제 1789번 그리디_수들의 합

문제에서 서로 다른 N개의 자연수의 합이 S라고 할경우에
N의 최댓값을 구하라는데 이런경우에는 
1부터 차근차근 더해 S가 될때까지 구해주면 된다.

작은수들부터 구해야 서로 다른 N개의 개수가 많아질테니 말이다.
문제 설명이 약간 부실했지만 좋았던 문제이다.

*/

#include <iostream>

using namespace std;
unsigned long long N, S;

int main() {
	cin >> S;
	unsigned long long total = 0;
	int result = 0;
	for (N = 1; N < S; N++) {
		total += N;
		if (total > S)
			break;
		result++;
	}

	cout << result << endl;

	return 0;
}