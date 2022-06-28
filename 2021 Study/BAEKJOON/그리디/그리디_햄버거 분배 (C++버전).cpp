#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);

	int n, k;
	cin >> n >> k;
	string temp;
	cin >> temp;
	
	vector<char> table(n);
	for (int i = 0; i < n; i++)
		table[i] = temp[i];

	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (table[i] == 'P') {
			for (int j = i - k; j < (i + k + 1); j++) {
				if ((j >= 0 && j < n) && (table[j] == 'H')) {
					answer++;
					table[j] = 'X';
					break;
				}
			}
		}
	}

	cout << answer << "\n";

	return 0;
}