public class Main {
    public static int solution(int n, int[] money) {
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for(int coin : money) {
            for(int price = coin; price < n + 1; ++price) {
                if(price >= coin)
                    dp[price] += dp[price - coin];
            }
        }

        return dp[n] % 1000000007;
    }

    public static void main(String[] args) {
        int n = 5;
        int[] money = {1, 2, 5};
        System.out.println(solution(n, money));
    }
}