/*
*
* 백준 문제 1010번 다리 놓기
*
* DP문제이다, 정확히 말하자면 조합을 활용한 DP 문제인데 조합을 몰라도 풀수있기는 하다.
* 근데 결국에는 DP 점화식을 만들면 조합의 원리대로 돌아간다.
*
* DP의 점화식은 이렇다.
* dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1]
* 여기서 dp[n][m - 1]은 dp[n][m]의 바로 전 까지 dp 됬던것, 즉 바로 전까지 다리를 놓았던것을 말한다.
* 중요한거는 dp[n - 1][m - 1] 이거인데 다리를 놓을때 한놈의 다리를 고정시켜놓고 나머지를 움직이는 경우라고 생각하면 된다.
* 그럼 끝이다.
*
* 아래처럼 DP로 풀어도 되지만, 조합을 써도 되는것을 안 이상 조합 식인 n! / r!(n - r)! 을 써서 문제를 풀어도된다.
* 팩토리얼쪽을 dp로 만들어서 풀면 더 빨리풀릴듯
* */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int t;

    private static void makeDP(int[][] dp) {
        for (int n = 1; n < 30; n++) {
            for (int m = 1; m < 30; m++) {
                if (n == 1)
                    dp[n][m] = m;
                else if (n == m)
                    dp[n][m] = 1;
                else {
                    dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1];
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        t = Integer.parseInt(st.nextToken());
        int[][] dp = new int[30][30];
        makeDP(dp);
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            System.out.println(dp[n][m]);
        }
    }
}