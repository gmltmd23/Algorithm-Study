/*
*
* 백준 문제 11866 자료 구조_요세푸스 문제0
*
* 자바 버전으로도 만들어보았다.
*
* */

import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> nums = new LinkedList<>();
        for (int i = 0; i < n; i++)
            nums.add(i + 1);

        StringBuilder sb = new StringBuilder();
        sb.append('<');

        while (nums.size() > 1) {
            for (int i = 0; i < k - 1; i++)
                nums.offer(nums.poll());
            sb.append(nums.poll()).append(", ");
        }
        sb.append(nums.poll()).append(">");
        System.out.println(sb);
    }
}