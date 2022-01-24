/*

(복습) 백준 문제 1149번 DP_RGB거리

매일 알고리즘 문제를 살펴보는건 쉬운일은 아니다만,
쉬지않고 하다보면 좋은일은 생길것이다.

*/

#include <iostream>
#include <algorithm>

using namespace std;
int house[1001][3];

int main() 
{
    int N;
    int cost[3];
    house[0][0] = 0;
    house[0][1] = 0;
    house[0][2] = 0;
    cin >> N;
    for (int i = 1; i <= N; ++i)
    {
        cin >> cost[0] >> cost[1] >> cost[2];
        house[i][0] = min(house[i - 1][1], house[i - 1][2]) + cost[0];
        house[i][1] = min(house[i - 1][0], house[i - 1][2]) + cost[1];
        house[i][2] = min(house[i - 1][1], house[i - 1][0]) + cost[2];
    }
    cout << min(house[N][2], min(house[N][0], house[N][1]));
}