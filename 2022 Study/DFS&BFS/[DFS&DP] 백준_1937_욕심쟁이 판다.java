import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        N = Integer.parseInt(br.readLine());
        bambooForest = new int[N][N];
        dp = new int[N][N];

        for(int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < N; ++j)
                bambooForest[i][j] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for(int x = 0; x < N; ++x) {
            for(int y = 0; y < N; ++y)
                answer = Math.max(answer, dfs(x, y));
        }

        System.out.println(answer);
    }

    public static int dfs(int x, int y) {
        if(dp[x][y] != 0)
            return dp[x][y] + 1;

        for(int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < N && 0 <= ny && ny < N) {
                if(bambooForest[nx][ny] > bambooForest[x][y])
                    dp[x][y] = Math.max(dp[x][y], dfs(nx, ny));
            }
        }

        return dp[x][y] + 1;
    }

    private static int N;
    private static int[][] bambooForest;
    private static int[][] dp;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
}