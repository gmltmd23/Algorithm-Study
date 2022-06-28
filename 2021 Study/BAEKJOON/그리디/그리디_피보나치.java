/*
*
* 백준 문제 9009번 그리디_피보나치
*
* 양의 정수 n이 주어지면 해당 n을 만들기 위해 가장 적은 갯수의 피보나치 수를 사용하여
* 그들의 합으로 n을 만드는 문제이다.
*
* 일단 n의 범위가 1 <= n <= 10억 이니깐 피보나치 수열을 10억이하의 숫자들로 만들어놓는다.
* 그리고 n보다는 작지만 n과 제일 가까운 피보나치 수 부터 거꾸로 거슬러 내려가 수들을 합쳐서 n을 만들어 주면 된다.
*
* 어려운 문제는 아니다. 다만 10억에 가까운 피보나치 수를 재귀함수로 구현하려면 (또 테스트 케이스가 여러개이기도 하고..)
* 시간효율성이 망해버릴테니깐 나처럼 DP로 피보나치 수열들을 구현해놓는것이 좋다.
*
* */

import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long[] fibo = new long[47]; // 어차피 n의 최대 범위는 10억까지니깐, 피보나치 수열로 만들수있는건 10억보다 작다.
        fibo[0] = 0;
        fibo[1] = 1;
        for (int i = 2; i < fibo.length; i++)
            fibo[i] = fibo[i - 1] + fibo[i - 2];

        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();

            int idx = 0;
            while (fibo[idx] <= n) { idx++; }

            long total = fibo[--idx];
            Stack<Long> stack = new Stack<>();
            stack.push(total);

            for (int j = --idx; j > 0; j--) {
                if (total + fibo[j] < n) {
                    total += fibo[j];
                    stack.push(fibo[j]);
                }
                else if (total + fibo[j] == n) {
                    stack.push(fibo[j]);
                    break;
                }
            }

            while (!stack.isEmpty()) {
                System.out.print(stack.pop() + " ");
            }
            System.out.print('\n');
        }
    }
}