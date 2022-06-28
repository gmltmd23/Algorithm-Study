/*
*
* 백준 문제 2012번 그리디_등수 매기기
*
* 파이썬으로 풀어보고 자바를 연습하기 위하여 자바로도 풀어봤다.
* 다만 자바로 풀때는 주의해야할 점이 있다.
*
* 불만도를 저장하는 변수의 타입을 long으로 설정해줘야 한다.
* 왜냐하면 주어진 scores 배열이 모두 500000으로 주어지면
* 불만도는 엄청나게 큰 수가 저장이 되어 int의 범위를 벗어날것이다.
* 그래서 long으로 지정해주면된다.
*
* */

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] scores = new int[N];
        long dissatisfaction = 0;
        for (int i = 0; i < N; i++)
            scores[i] = sc.nextInt();
        Arrays.sort(scores);

        for (int i = 0; i < N; i++) {
            if ((i + 1) != scores[i]) {
                dissatisfaction += Math.abs(scores[i] - (i + 1));
            }
        }

        System.out.println(dissatisfaction);
        sc.close();
    }
}