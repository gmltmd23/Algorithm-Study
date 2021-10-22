/*
*
* 백준 문제 14720번 그리디_우유 축제
*
* 아주 EEEEEEEEasy한 그리디문제이다.
* 자신의 현재 턴에 맞춰서 우유를 먹기만 하면된다.
* 다만 우유의 종류가 3가지니깐 turn이 3이되면 0으로 다시 초기화를 해주는것이 포인트!
*
* */

import java.util.*;
import java.io.*;

class Main {
    private static int N;
    private static int turn; // 0 = 딸기우유, 1 = 초코우유, 2 = 바나나우유

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int answer = 0;
        for (int i = 0; i < N; i++) {
            int store = Integer.parseInt(st.nextToken());
            if (store == turn) {
                answer++;
                turn = (turn == 2) ? 0 : (turn + 1);
            }
        }

        System.out.print(answer + "\n");
    }
}