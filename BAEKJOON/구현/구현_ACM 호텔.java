/*
*
* 백준 문제 10250번 ACM 호텔
*
* 아주 EEEEEasy한 구현 문제이다.
* 근데 정답률 낮은거보면 사람들이 구현 문제를 많이 연습안하는것 같다.
* 기본적으로 사고력을 키우는데 좋은문제
*
* */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            if (n % h == 0)
                System.out.println((h * 100) + (n / h));
            else
                System.out.println(((n % h) * 100) + ((n / h) + 1));
        }
    }
}