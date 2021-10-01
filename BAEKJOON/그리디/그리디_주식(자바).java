/*
*
* 백준 문제 11501번 그리디_주식
*
* 파이썬으로 풀었었던 문제이다.
* 자바도 연습할 필요성이 있어서 자바로도 만들어보았다.
* 꾸준히 연습하자.
*
* */

import java.util.*;

class Main {
    private static final Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int testCase = sc.nextInt();
        for (int t = 0; t < testCase; t++) {
            long profit = 0;
            int days = sc.nextInt();
            long[] stocks = new long[days];
            for (int i = 0; i < days; i++)
                stocks[i] = sc.nextInt();

            long maximum = 0;
            for (int i = stocks.length - 1; i >= 0; i--) {
                if (stocks[i] <= maximum)
                    profit += (maximum - stocks[i]);
                else
                    maximum = stocks[i];
            }
        System.out.print(profit + "\n");
        }
    }
}