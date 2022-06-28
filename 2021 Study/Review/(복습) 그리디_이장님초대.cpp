/*

(복습) 백준 문제 9237번 그리디_이장님 초대

나무가 걸리는 시간을 거꾸로 받는것이 포인트인 문제였다.

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N; 
vector<int> v;

int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}
	sort(v.rbegin(), v.rend());

	int days = 0;
	for (int i = 0; i < N; i++)
	{
		days = max(days, v[i] + i + 1);
	}

	cout << days + 1;

	return 0;
}