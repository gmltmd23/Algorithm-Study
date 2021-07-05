/*
*
* 백준 10809번 알파벳 찾기
*
* 쉬운 문제였다. 자바로도 틈틈히 푸는것을 연습해둬야겠다.
*
* */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static char[] str;
    private static int[] alphabet;

    private static void make_alphabet() {
        alphabet = new int[26];
        Arrays.fill(alphabet, -1);
    }

    public static void main(String[] args) throws IOException {
        str = new BufferedReader(new InputStreamReader(System.in)).readLine().toCharArray();
        make_alphabet();
        for (int i = 0; i < str.length; i++) {
            if (alphabet[(int)str[i] - 97] == -1) {
                alphabet[(int)str[i] - 97] = i;
            }
        }

        for (int value : alphabet) {
            System.out.print(value + " ");
        }
    }
}