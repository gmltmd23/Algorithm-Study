/*

���� ���� 5014�� �׷��� Ž��_��ŸƮ��ũ

ó������ �� ����� �ؾߵǴ� BFS �����̴�.
apartment �迭�� �����Ͽ� �̰��� ��ư�� ������ Ƚ���� �����ϰ�,
u, d�� �迭�� ���� ���� bfs������ ������ �ȴ�.

�ٵ�.. �и��� �ڵ尡 �´µ� ��� Ʋ���ٰ� ���Դ�.
�̰� Ʋ�� �ڵ尡 �ƴѵ�..

��Ż�� ������ ������ �ٽ� �ѹ� �о�ô���
�ش� ���� �������� ���Ұ�쿡 "use the stairs"�� ����϶�� ���ִµ�
���� "use the stair"�� ����ߴ� ��������������������������
���� s �ѱ��� ���Ծ ���� �ð� 10������ �� �����Ű��� �Ф�

�������� ������ �� �� �ڼ��� ����.

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