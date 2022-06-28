/*

(복습) 백준 문제 1916번 그래프탐색_최소비용 구하기

다익스트라 문제이다.
다익스트라의 기초를 상기시키기 좋은문제!

*/

#include <iostream>
#include <queue>
#include <vector>
#define MAX 1001
#define BMAX 100001
#define INF 987654321
using namespace std;

int n, m;
vector<pair<int, int>> Bus[MAX];
int start, destination;
int dist[MAX];

void Input() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        Bus[a].push_back(make_pair(b, c));
    }
    cin >> start >> destination;
    for (int i = 1; i <= n; i++) {
        dist[i] = INF;
    }
}

void Dijkstra() {
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(0, start));
    dist[start] = 0;
    while (!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if (dist[cur] < cost)
            continue;
        for (int i = 0; i < Bus[cur].size(); i++) {
            int next = Bus[cur][i].first;
            int ncost = cost + Bus[cur][i].second;
            if (dist[next] > ncost) {
                dist[next] = ncost;
                pq.push(make_pair(-ncost, next));
            }
        }
    }
    cout << dist[destination] << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Dijkstra();
    return 0;
}