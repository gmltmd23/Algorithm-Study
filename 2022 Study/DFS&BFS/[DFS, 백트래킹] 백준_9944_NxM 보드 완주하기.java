import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int INF = 1000001;
    private static int n, m;
    private static boolean[][] graph;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    private static void dfs(final int x, final int y, final int direction, int counter, int[] minimumMoveCount) {
        int nx = (x + dx[direction]);
        int ny = (y + dy[direction]);
        if(0 <= nx && nx < n && 0 <= ny && ny < m && !graph[nx][ny]) {
            graph[nx][ny] = true;
            dfs(nx, ny, direction, counter, minimumMoveCount);
            graph[nx][ny] = false;
        }
        else { // 다른 방향 찾기
            boolean isEnd = true;
            for(int i = 0; i < 4; ++i) {
                if(i == direction)
                    continue;
                nx = (x + dx[i]);
                ny = (y + dy[i]);
                if(0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if(!graph[nx][ny]) {
                        graph[nx][ny] = true;
                        dfs(nx, ny, i, counter + 1, minimumMoveCount);
                        isEnd = false;
                        graph[nx][ny] = false;
                    }
                }
            }

            if(isEnd) {
                for(int checkX = 0; checkX < n; ++checkX) {
                    for(int checkY = 0; checkY < m; ++checkY) {
                        if(!graph[checkX][checkY])
                            return;
                    }
                }

                minimumMoveCount[0] = Math.min(minimumMoveCount[0], counter);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> resultList = new ArrayList<>();
        StringTokenizer st = null;

        while(true) {
            st = new StringTokenizer(br.readLine(), " ");
            if(!st.hasMoreTokens())
                break;

            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            graph = new boolean[n][m]; // true == star, false = empty
            for(int i = 0; i < n; ++i) {
                String line = br.readLine();
                for(int j = 0; j < m; ++j) {
                    if(line.charAt(j) == '*')
                        graph[i][j] = true;
                }
            }

            int[] minimumMoveCount = new int[1];
            minimumMoveCount[0] = INF;
            for(int x = 0; x < n; ++x) {
                for(int y = 0; y < m; ++y) {
                    if(!graph[x][y]) {
                        graph[x][y] = true;
                        for(int i = 0; i < 4; ++i) {
                            int nx = (x + dx[i]);
                            int ny = (y + dy[i]);
                            if(nx < 0 || nx >= n || ny < 0 || ny >= m)
                                continue;
                            if(graph[nx][ny])
                                continue;
                            graph[nx][ny] = true;
                            dfs(nx, ny, i, 1, minimumMoveCount);
                            graph[nx][ny] = false;
                        }
                        graph[x][y] = false;
                    }
                }
            }

            resultList.add((minimumMoveCount[0] == INF) ? -1 : minimumMoveCount[0]);
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < resultList.size(); ++i)
            sb.append("Case " + (i + 1) + ": " + resultList.get(i) + "\n");
        System.out.print(sb.toString());

        br.close();
    }
}