/*
*
* 백준 문제 2941번 크로아티아 알파벳
*
* 이것도 구현 문제이다.
* 쓸데없는 루프를 돌리지말고 시간복잡도 O(n)으로만 풀면 되는 문제이다.
* 확실히 파이썬쓰다가 자바로 알고리즘 문제 풀려고 보니
* 자바보다는 파이썬쪽이 코드가 더 깔끔하고 간결하게 나오긴하는거같다.
*
* */

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(solution(sc.next().trim().toCharArray()));
    }

    private static int solution(char[] data) {
        int result = 0;
        int idx = 0;
        while (idx < data.length) {
            if (idx + 1 != data.length) {
                switch (data[idx]) {
                    case 'c':
                        if (data[idx + 1] == '=' || data[idx + 1] == '-')
                            idx++;
                        break;
                    case 'd':
                        if (data[idx + 1] == 'z') {
                            if (idx + 2 != data.length && data[idx + 2] == '=')
                                idx += 2;
                        }
                        else if (data[idx + 1] == '-')
                            idx++;
                        break;
                    case 'l':
                    case 'n':
                        if (data[idx + 1] == 'j')
                            idx++;
                        break;
                    case 's':
                    case 'z':
                        if (data[idx + 1] == '=')
                            idx++;
                        break;
                }
            }
            result++;
            idx++;
        }
        return result;
    }
}