/*

拷層 庚薦 5014腰 益掘覗 貼事_什展闘元滴

坦製拭澗 岨 壱肯聖 背醤鞠澗 BFS 庚薦戚陥.
apartment 壕伸聖 識情馬食 戚員拭 獄動聖 刊牽澗 判呪研 煽舌馬壱,
u, d研 壕伸稽 幻級嬢辞 汝雌獣 bfs床牛戚 宜軒檎 吉陥.

悦汽.. 歳誤備 坪球亜 限澗汽 域紗 堂軒陥壱 蟹尽陥.
戚惟 堂険 坪球亜 焼観汽..

伍纏戚 凹閃辞 庚薦研 陥獣 廃腰 石嬢挫希艦
背雁 寵拭 亀鐸馬走 公拝井酔拭 "use the stairs"研 窒径馬虞壱 鞠赤澗汽
蟹澗 "use the stair"研 窒径梅陥 せせせせせせせせせせせせせ
魁拭 s 廃越切 皐股嬢辞 右備 獣娃 10歳舛亀 希 劾鍵暗旭陥 ばば

陥製拭澗 庚薦研 岨 希 切室備 石切.

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