/*

(복습) 백준 문제 2109번 그리디_순회 강연

우선순위큐를 활용한 그리디 문제이다.
자료구조 문제라고 봐도 무방할듯하다.

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int n;
priority_queue<int, vector<int>, greater<int>> pq;
vector<pair<int, int>> v;
int result;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int p, d;
        cin >> p >> d;
        v.push_back(make_pair(d, p));
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++) {
        pq.push(v[i].second);
        result += v[i].second;

        if (pq.size() > v[i].first) {
            result -= pq.top();
            pq.pop();
        }
    }

    cout << result;

    return 0;
}
