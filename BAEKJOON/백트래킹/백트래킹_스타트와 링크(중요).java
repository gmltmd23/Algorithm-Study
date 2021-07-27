/*
*
* 백준 문제 14889번 스타트와 링크
*
* 다 이해하고보니깐 난이도는 높지않은 문제인데
* 백트래킹 문제 자체를 많이 안풀어봐서, 백트래킹 구현부분에서 곤란했던 문제다.
* 반드시 복습!
*
* */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    static int N;
    static int[][] map;
    static boolean[] team;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        map = new int[N][N];
        team = new boolean[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve(0,0);
        System.out.println(min);
    }

    static void solve(int cnt, int cur) {

        if(cnt == N/2) {
            int sumA = 0;
            int sumB = 0;

            for (int i = 0; i < N; i++) {
                for (int j = i+1; j < N; j++) {
                    if(team[i] != team[j])
                        continue;
                    if(team[i]) {
                        sumA += map[i][j] + map[j][i];
                    }
                    else {
                        sumB += map[i][j] + map[j][i];
                    }
                }
            }
            min = Math.min(min, Math.abs(sumA-sumB));
            return;
        }

        for (int i = cur; i < N; i++) {
            team[i] = true;
            solve(cnt+1,i+1);
            team[i] = false;
        }
    }

}
