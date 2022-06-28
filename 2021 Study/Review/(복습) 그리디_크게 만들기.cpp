/*

(����) ���� ���� 2812�� �׸���_ũ�� �����

������ �̿��ؼ� ū ���� �ɷ����°��� �ٽ��̴�.

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