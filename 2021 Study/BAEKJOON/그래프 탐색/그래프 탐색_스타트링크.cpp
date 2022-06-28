/*

백준 문제 5014번 그래프 탐색_스타트링크

처음에는 좀 고민을 해야되는 BFS 문제이다.
apartment 배열을 선언하여 이곳에 버튼을 누르는 횟수를 저장하고,
u, d를 배열로 만들어서 평상시 bfs쓰듯이 돌리면 된다.

근데.. 분명히 코드가 맞는데 계속 틀리다고 나왔다.
이게 틀릴 코드가 아닌데..

멘탈이 깨져서 문제를 다시 한번 읽어봤더니
해당 층에 도착하지 못할경우에 "use the stairs"를 출력하라고 되있는데
나는 "use the stair"를 출력했다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
끝에 s 한글자 빼먹어서 괜히 시간 10분정도 더 날린거같다 ㅠㅠ

다음에는 문제를 좀 더 자세히 읽자.

*/

#include <iostream>
#include <queue>

#define MAX 1000000
#define endl '\n'
using namespace std;

int f, s, g, u, d;
int apartment[MAX + 1];

void input() {
	cin >> f >> s >> g >> u >> d;
	for (int i = 0; i < MAX + 1; i++)
		apartment[i] = MAX;
	apartment[s] = 0;
}

int bfs() {
	int dir[2] = { u, -d };
	queue<int> q;
	q.push(s);

	while (!q.empty()) {
		int now_stair = q.front();
		q.pop();
		
		for (int i = 0; i < 2; i++) {
			int next_stair = now_stair + dir[i];
			if (next_stair < 1 || next_stair > f)
				continue;
			if (apartment[now_stair] + 1 < apartment[next_stair]) {
				apartment[next_stair] = apartment[now_stair] + 1;
				q.push(next_stair);
			}
		}
	}

	return apartment[g];
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	input();
	
	int answer = bfs();
	if (answer == MAX)
		cout << "use the stairs" << endl;
	else
		cout << answer << endl;

	return 0;
}