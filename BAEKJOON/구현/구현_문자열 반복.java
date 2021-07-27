/*
*
* 백준 문제 2675번 문자열 반복
*
* 요즘 구현문제를 많이안풀어서 한동안은 구현문제좀 풀어봐야겠다.
* 간단한 구현문제였다.
*
* */

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int count = sc.nextInt();
            String temp = "";
            for (char c : sc.next().toCharArray()) {
                temp += repeat(c, count);
            }
            System.out.println(temp);
        }
    }

    private static String repeat(char c, int count) {
        String temp = "";
        for (int i = 0; i < count; i++) {
            temp += c;
        }
        return temp;
    }
}