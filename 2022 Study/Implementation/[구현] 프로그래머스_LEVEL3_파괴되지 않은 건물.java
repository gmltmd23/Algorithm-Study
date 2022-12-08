import java.util.*;

public class Main {
    public static int solution(int[][] board, int[][] skill) {
        int n = board.length;
        int m = board[0].length;
        int[][] accumulationBoard = new int[n][m];

        for(int[] eachSkill : skill) {
            int type, r1, c1, r2, c2, degree;
            type = eachSkill[0]; r1 = eachSkill[1]; c1 = eachSkill[2]; r2 = eachSkill[3]; c2 = eachSkill[4]; degree = eachSkill[5];

            int weight = (type == 1) ? -degree : degree;
            accumulationBoard[r1][c1] += weight;

            if((c2 + 1) < m)
                accumulationBoard[r1][c2 + 1] += (-weight);
            if((r2 + 1) < n)
                accumulationBoard[r2 + 1][c1] += (-weight);
            if((c2 + 1) < m && (r2 + 1) < n)
                accumulationBoard[r2 + 1][c2 + 1] += weight;
        }

        for(int x = 0; x < n; ++x) {
            for(int y = 0; y < (m - 1); ++y)
                accumulationBoard[x][y + 1] += accumulationBoard[x][y];
        }
        for(int y = 0; y < m; ++y) {
            for(int x = 0; x < (n - 1); ++x)
                accumulationBoard[x + 1][y] += accumulationBoard[x][y];
        }

        int answer = n * m;
        for(int x = 0; x < n; ++x) {
            for(int y = 0; y < m; ++y) {
                if((board[x][y] + accumulationBoard[x][y]) <= 0)
                    --answer;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[][] board = {
                {5,5,5,5,5},
                {5,5,5,5,5},
                {5,5,5,5,5},
                {5,5,5,5,5}
        };
        int[][] skill = {
                {1,0,0,3,4,4},
                {1,2,0,2,3,2},
                {2,1,0,3,1,2},
                {1,0,1,3,3,1}
        };

        System.out.println(solution(board, skill));
    }
}