/*

(복습) 프로그래머스 DP_N으로 표현

높은 난이도의 DP문제였다.
예전에 풀때도 난이도가 높았지만, 지금 풀어도 까다로운 문제는 맞다.
그래도 복습을 하니, 풀리긴 해서 다행이다.

*/

#include <vector> 
#include <unordered_set> 
using namespace std;

int getN(int N, int idx) {
    int result = N;
    for (int i = 1; i <= idx; i++) {
        result = result * 10 + N;
    }
    return result;
}

int solution(int N, int number) {
    if (N == number)
        return 1;

    vector<unordered_set<int>> DP(8);
    DP[0].insert(N); 
    for (int k = 1; k < 8; k++) {
        DP[k].insert(getN(N, k));
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                if (i + j + 1 != k) 
                    continue;
                for (int a : DP[i]) {
                    for (int b : DP[j]) {
                        DP[k].insert(a + b);

                        if (a - b > 0)
                            DP[k].insert(a - b);
                        DP[k].insert(a * b);

                        if (a / b > 0) DP[k].insert(a / b);
                    }
                }
            }
        }

        if (DP[k].find(number) != DP[k].end())
            return k + 1;
    }
    return -1;
}