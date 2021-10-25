/*
*
* 백준 문제 16435번 그리디_스네이크버드
*
* 가끔은 이렇게 쉬운문제 풀어도 괜찮잖아??? ㅋㅋㅋㅋㅋㅋㅋㅋ
* 아주 가벼운 문제였다.
*
* 다만 문제에 설명이 좀 빈약해서, fruits들을 그냥 받아서
* 인덱스 순차적으로 진행하면 될줄 알았는데 sort해서 먹을수있는 만큼 최대한 먹어야되는 문제였다.
*
* 그리디 문제가 알고리즘 실력을 유지하는데 가장 도움이 되는 것 같다.
*
* */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] fruits = new int[N];
        for (int i = 0; i < N; i++)
            fruits[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(fruits);

        for (int fruit : fruits)
            if (L >= fruit) L++;

        System.out.print(L);
        br.close();
    }
}