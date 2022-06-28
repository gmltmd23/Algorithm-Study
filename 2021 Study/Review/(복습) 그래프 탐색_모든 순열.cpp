/*

(복습) 백준 문제 10974번 그래프탐색_모든 순열

예전에는 visited를 이용해서 구해서 이번에는 permutation을 이용해서
구해보았다!

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> a;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) a.push_back(i + 1);
    do {
        for (int i = 0; i < n; i++) {
            cout << a[i] << " ";
        }
        cout << "\n";
    } while (next_permutation(a.begin(), a.end()));
}