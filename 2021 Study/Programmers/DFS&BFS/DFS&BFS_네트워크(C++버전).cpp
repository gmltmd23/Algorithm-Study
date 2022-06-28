/*

프로그래머스 DFS&BFS_네트워크 : LEVEL 3 (C++ 버전)

C++의 감을 잊지않기 위해서 기존에 짰던 코드를 리팩토링 해보았다.
복습겸 좋은것 같다.

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