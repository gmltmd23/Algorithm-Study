import java.util.*;

public class Main {
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static class Point {
        public int x;
        public int y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[][] costMap = new int[n][m];

        costMap[0][0] = 1;
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0, 0));

        while(!q.isEmpty()) {
            Point nowPoint = q.poll();
            int x = nowPoint.x;
            int y = nowPoint.y;

            for(int i = 0; i < 4; ++i) {
                int nx = (x + dx[i]);
                int ny = (y + dy[i]);

                if(0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if(maps[nx][ny] == 1 && costMap[nx][ny] == 0) {
                        costMap[nx][ny] = costMap[x][y] + 1;
                        q.add(new Point(nx, ny));
                    }
                }
            }
        }

        return (costMap[n - 1][m - 1] == 0) ? -1 : costMap[n - 1][m - 1];
    }

    public static void main(String[] args) {
        int[][] maps = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,1}, {0,0,0,0,1}};
        System.out.println(solution(maps));
    }
}