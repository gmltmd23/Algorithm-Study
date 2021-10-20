/*
*
* 백준 문제 1758번 그리디_알바생 강호
*
* 정답률 38.241%의 문제인데 왜 정답률이 낮은지 모르겠다.
* 어려운 문제가 아니다.
* 그리디 문제들이 대부분 그러하듯 핵심적인 큰 것을 해결하면 작은 것은 자동으로 해결된다.
*
* 이 문제는 받은 tips의 값들을 정렬을 시킨 뒤 가장 큰 값부터 1등으로 쭉쭉 보내면 된다.
* 파이썬같은것으로 풀이를 할때에는 문제가 없겠지만, 자료형이 존재하는 랭귀지로 풀때는
* total의 값을 long이나 unsigned long long, 아니면 long long
* 또는 자바에서는 BigInteger를 활용해서 푸는것도 나쁘지는 않다.
*
* 팁의 범위가 100,000 까지는 가기때문에 total의 값이 최악의 경우 10^5 * 10^5 이 될수가 있기 때문이다.
*
* */

import java.util.*;
import java.io.*;

class Main {
    private static void solution(int N, int[] tips) {
        Arrays.sort(tips);

        int minus = 0;
        long total = 0;
        for (int i = tips.length - 1; i >= 0; i--) {
            int result = tips[i] - minus++;
            if (result > 0)
                total += result;
            else
                break;
        }

        System.out.print(total + "\n");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] tips = new int[N];
        for (int i = 0; i < N; i++)
            tips[i] = Integer.parseInt(br.readLine());

        solution(N, tips);
    }
}