/*

(����) ���� ���� 10974�� �׷���Ž��_��� ����

�������� visited�� �̿��ؼ� ���ؼ� �̹����� permutation�� �̿��ؼ�
���غ��Ҵ�!

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