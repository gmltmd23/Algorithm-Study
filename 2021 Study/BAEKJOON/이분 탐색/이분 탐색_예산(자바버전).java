/*
*
* 백준 2512 예산
*
* 자바도 연습을 해야되서 자바 버전으로도 만들어봤다.
*
* */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Algorithm {
    static int n;
    static int budget;
    static int[] request;

    public static void main(String[] args) throws IOException {
        int maximumCost = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        n = Integer.parseInt(st.nextToken());
        request = new int[n];
        st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < n; i++) {
            request[i] = Integer.parseInt(st.nextToken());
            maximumCost = Math.max(maximumCost, request[i]);
        }
        budget = Integer.parseInt((new StringTokenizer(br.readLine().trim())).nextToken());

        int criteria = (budget / n);
        for (int req : request) {
            if (req <= criteria) {
                n--;
                budget -= req;
            }
        }

        int newCriteria = (n == 0) ? maximumCost : (budget / n);
        System.out.print((maximumCost > newCriteria) ? newCriteria : maximumCost);
    }
}
