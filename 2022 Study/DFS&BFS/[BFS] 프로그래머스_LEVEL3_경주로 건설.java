import java.util.*;

public class Main {
    static class State {
        public int x;
        public int y;
        public int dir;
        public int cost;

        public State(int x, int y, int dir, int cost) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.cost = cost;
        }
    }

    private static final int INF = Integer.MAX_VALUE;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    public static int solution(int[][] board) {
        int N = board.length;
        Deque<State> q = new ArrayDeque<>();
        q.add(new State(0, 0, -1, 0));

        int[][][] costBoard = new int[4][N][N];
        for(int k = 0 ; k < 4; ++k) {
            for(int i = 0; i < N; ++i) {
                for(int j = 0; j < N; ++j)
                    costBoard[k][i][j] = INF;
            }
            costBoard[k][0][0] = 0;
        }

        while(!q.isEmpty()) {
            State nowState = q.pollFirst();
            for(int dir = 0; dir < 4; ++dir) {
                int nx = nowState.x + dx[dir];
                int ny = nowState.y + dy[dir];
                if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                    continue;
                if(board[nx][ny] == 1)
                    continue;

                int nextCost = nowState.cost;
                if(nowState.dir == -1 || nowState.dir == dir)
                    nextCost += 100;
                else
                    nextCost += 600;

                if(nextCost <= costBoard[dir][nx][ny]) {
                    costBoard[dir][nx][ny] = nextCost;
                    q.add(new State(nx, ny, dir, nextCost));
                }
            }
        }

        int answer = INF;
        for(int i = 0; i < 4; ++i)
            answer = Math.min(answer, costBoard[i][N - 1][N - 1]);

        return answer;
    }

    public static void main(String[] args) {
        int[][] board = { {0, 0, 0, 0, 0, 0, 0, 0},
                        {1, 0, 1, 1, 1, 1, 1, 0},
                        {1, 0, 0, 1, 0, 0, 0, 0},
                        {1, 1, 0, 0, 0, 1, 1, 1},
                        {1, 1, 1, 1, 0, 0, 0, 0},
                        {1, 1, 1, 1, 1, 1, 1, 0},
                        {1, 1, 1, 1, 1, 1, 1, 0},
                        {1, 1, 1, 1, 1, 1, 1, 0} };

        System.out.println(solution(board));
    }
}