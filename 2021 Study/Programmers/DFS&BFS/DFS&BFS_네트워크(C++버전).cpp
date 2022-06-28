/*

���α׷��ӽ� DFS&BFS_��Ʈ��ũ : LEVEL 3 (C++ ����)

C++�� ���� �����ʱ� ���ؼ� ������ ®�� �ڵ带 �����丵 �غ��Ҵ�.
������ ������ ����.

*/

#include <string>
#include <vector>

using namespace std;

void dfs(int n, vector<vector<int>> &computers, int i) {
    computers[i][i] = 0;
    for (int j = 0; j < n; j++) {
        if (computers[i][j] == 1) {
            computers[i][j] = 0;
            dfs(n, computers, j);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (computers[i][i] == 1) {
            dfs(n, computers, i);
            answer++;
        }
    }

    return answer;
}