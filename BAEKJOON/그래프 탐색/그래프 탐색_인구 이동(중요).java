/*
*
* 백준 문제 16234번 그래프 이론_인구 이동
*
* 정답률 35.746%이고, 난이도가 있는 DFS/BFS 문제이다.
* 근데 DFS/BFS는 난이도가 이정도는 되줘야 푸는데 재미가 있긴함, 문제들이 거의 다 공식처럼 되있어서ㅋㅋㅋ
*
* 이 문제의 핵심은 DFS/BFS로 영역(연합)을 찾고(만약 연합이 존재하면 true 리턴), 그 영역들에 속하는 Element 값들의 총합을 Element의 개수로 나누고
* 그 값들을 각각의 Element에 할당시켜준다. (연합이 없었다면 false를 리턴 했을것이다.)
*
* true를 리턴받으면 연합이 존재해서 인구이동이 발생했다는 뜻이니깐 count값을 +1하고 인구 이동으로 인해 연합에 변화가 생겼을 수도 있으니 루프 한번 더
* false를 리턴받으면 연합이 더 이상 존재하지 않다는 뜻이니깐 지금까지 모아진 count 값을 리턴하면 정답이다.
*
* */

import java.util.*;
import java.io.*;

class Main {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static int N, L, R;
    private static int[][] map;
    private static boolean[][] visited;
    private static Queue<Point> q;
    private static List<Point> group;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        q = new LinkedList<>();
        group = new LinkedList<>();
        map = new int[N][N];

        for (int x = 0; x < N; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < N; y++)
                map[x][y] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solution());
        br.close();
    }

    static int solution() {
        int count = 0;
        boolean isMove;

        while(true) {
            visited = new boolean[N][N];
            isMove = false;
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    if (visited[x][y]) continue;
                    if (bfs(x, y)) isMove = true;
                }
            }

            if (isMove) count++;
            else return count;
        }
    }

    static boolean bfs(int x, int y) {
        q.clear();
        group.clear();

        q.add(new Point(x, y));
        group.add(new Point(x, y));
        visited[x][y] = true;
        int total = map[x][y];

        while (!q.isEmpty()) {
            Point point = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = point.x + dx[i];
                int ny = point.y + dy[i];
                if (((0 <= nx) && (nx < N)) && ((0 <= ny)&& (ny < N))) {
                    int diff = Math.abs(map[point.x][point.y] - map[nx][ny]);
                    if ((!visited[nx][ny]) && ((diff >= L) && (diff <= R))) {
                        q.add(new Point(nx, ny));
                        group.add(new Point(nx, ny));
                        visited[nx][ny] = true;
                        total += map[nx][ny];
                    }
                }
            }
        }

        if (group.size() <= 1)
            return false;
        else {
            int people = total / group.size();
            for (Point p : group)
                map[p.x][p.y] = people;
            return true;
        }
    }

    static class Point {
        private int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}