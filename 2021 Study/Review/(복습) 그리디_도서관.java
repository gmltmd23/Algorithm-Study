/*
*
* 백준 문제 1461번 그리디_도서관
*
* 그리디를 푸는법은 가장 오래걸리는것(큰것) 먼저 해결하는것이 중요하다.
* 이 문제의 힌트는 책을 모두 제자리에 둔 후에는 다시 0으로 돌아 올 필요가 없다는 것이다.
* 보통 좌표를 다녀오면 그 좌표를 찍고, 0으로 다시 가야되기때문에 값은 좌표 * 2가 된다.
* 그렇지만 가장 큰 값을 가장 마지막에 다녀오는것처럼 처리 하게되면 가장 큰값은 한번만 더해도 되니깐 걸음 수가 줄어들게된다.
* 저 가장 큰값만 처리하게되면 나머지는 배열이 빌때까지 그냥 쭉 다녀오면 된다.
*
* */

import java.util.*;
import java.io.*;

class Main {
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        LinkedList<Integer> minus = new LinkedList<>();
        LinkedList<Integer> plus = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(st.nextToken());
            if (temp > 0) plus.add(temp);
            else minus.add(-temp);
        }
        plus.sort(Comparator.reverseOrder());
        minus.sort(Comparator.reverseOrder());

        int[] answer = new int[1];
        if (!minus.isEmpty() && !plus.isEmpty()) {
            if (plus.peek() > minus.peek()) {
                answer[0] += plus.poll();
                for (int i = 0; i < M - 1; i++)
                    plus.poll();
            }
            else {
                answer[0] += minus.poll();
                for (int i = 0; i < M - 1; i++)
                    minus.poll();
            }
        }
        else if (!minus.isEmpty() && plus.isEmpty()) {
            answer[0] += minus.poll();
            for (int i = 0; i < M - 1; i++)
                minus.poll();
        }
        else if (minus.isEmpty() && !plus.isEmpty()) {
            answer[0] += plus.poll();
            for (int i = 0; i < M - 1; i++)
                plus.poll();
        }

        process(answer, plus);
        process(answer, minus);

        System.out.println(answer[0]);
        br.close();
    }

    static void process(int[] answer, LinkedList<Integer> arr) {
        while (!arr.isEmpty()) {
            if (arr.size() >= M) {
                answer[0] += arr.poll() * 2;
                for (int i = 0; i < M - 1; i++)
                    arr.poll();
            }
            else {
                answer[0] += arr.poll() * 2;
                while (!arr.isEmpty())
                    arr.poll();
            }
        }
    }
}