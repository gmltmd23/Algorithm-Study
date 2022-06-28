/*
*
* 백준 16953번 A -> B
*
* A 숫자를 2가지 연산을 써서 B 숫자로 만드는 문제이다.
* 그런데 A를 B로 만드는것보다 B를 A로 만드는 아이디어를 떠올리면 풀 수 있는 문제이다.
*
* */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static String a;
    static String b;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int count = 0;
        a = st.nextToken();
        b = st.nextToken();
        int parsed_b = Integer.parseInt(b);

        while (parsed_b > Integer.parseInt(a)) {
            if (parsed_b % 2 == 0) {
                parsed_b = parsed_b / 2;
            } else {
                String temp = Integer.toString(parsed_b);
                if (temp.charAt(temp.length() - 1) == '1') {
                    parsed_b = Integer.parseInt(temp.substring(0, temp.length() - 1));
                } else {
                    parsed_b = -1;
                    break;
                }
            }
            count++;
        }
        System.out.print((parsed_b == Integer.parseInt(a)) ? ++count : -1);
    }
}