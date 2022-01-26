/*

(복습) 백준 문제 2812번 그리디_크게 만들기

스택을 이용해서 큰 값을 걸러내는것이 핵심이다.

*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int n, k;
string num;
vector<char> orig;
vector<char> result;

void Input() {
    cin >> n >> k;
    cin >> num;
    for (int i = 0; i < n; i++) {
        orig.push_back(num[i]);
    }
}

void Solution() {
    int idx = 0;
    while (idx != num.size()) {
        while (k != 0 && !result.empty() && result.back() < orig[idx]) {
            result.pop_back();
            k--;
        }
        result.push_back(orig[idx]);
        idx++;
    }
    while (k--) {
        result.pop_back();
    }
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}