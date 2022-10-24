public class Main {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static int n;
    private static int answer = Integer.MAX_VALUE;

    private static boolean isTwelveClock(int[][] clockHands) {
        int twelveCounter = 0;
        for(int x = 0; x < n; ++x) {
            for(int y = 0; y < n; ++y) {
                if(clockHands[x][y] == 0)
                    ++twelveCounter;
            }
        }
        return (twelveCounter == (n * n));
    }

    private static void turnClock(int[][] clockHands, int x, int y, boolean clockwise) {
        clockHands[x][y] += (clockwise) ? 1 : -1;
        clockHands[x][y] = (clockHands[x][y] < 0) ? 3 : (clockHands[x][y] % 4);

        for(int i = 0; i < 4; ++i) {
            int nx = (x + dx[i]);
            int ny = (y + dy[i]);
            if(0 <= nx && nx < n && 0 <= ny && ny < n) {
                clockHands[nx][ny] += (clockwise) ? 1 : -1;
                clockHands[nx][ny] = (clockHands[nx][ny] < 0) ? 3 : (clockHands[nx][ny] % 4);
            }
        }
    }

    private static boolean isTarget(int[][] clockHands, int x, int y) {
        if(clockHands[x][y] == 0)
            return false;

        for(int i = 0; i < 4; ++i) {
            int nx = (x + dx[i]);
            int ny = (y + dy[i]);
            if(0 <= nx && nx < n && 0 <= ny && ny < n) {
                if(clockHands[nx][ny] == 0)
                    return false;
            }
        }
        return true;
    }

    private static void dfs(int[][] clockHands, int count) {
        if(isTwelveClock(clockHands)) {
            answer = Math.min(answer, count);
            return;
        }

        for(int x = 0; x < n; ++x) {
            for(int y = 0; y < n; ++y) {
                if(isTarget(clockHands, x, y)) {
                    turnClock(clockHands, x, y, true);
                    dfs(clockHands, count + 1);
                    turnClock(clockHands, x, y, false);
                }
            }
        }
    }

    private static int solution(int[][] clockHands) {
        n = clockHands.length;
        dfs(clockHands, 0);
        return answer;
    }

    public static void main(String[] args) {
        int[][] clockHands = {{0,3,3,0}, {3,2,2,3}, {0, 3, 2, 0}, {0, 3, 3, 3}};
        System.out.println(solution(clockHands));
    }
}