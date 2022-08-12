import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        graph = new char[r][c];
        visited = new boolean[26];

        for(int i = 0; i < r; ++i) {
            String line = br.readLine();
            for(int j = 0; j < c; ++j)
                graph[i][j] = line.charAt(j);
        }

        result = 1;
        visited[getIndex(graph[0][0])] = true;
        dfs(0, 0, 1);

        System.out.print(result + "\n");
    }

    public static void dfs(final int x, final int y, final int count) {
        boolean hasNext = false;
        for(int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < r && 0 <= ny && ny < c) {
                int nextAlphabetIndex = getIndex(graph[nx][ny]);
                if(!visited[nextAlphabetIndex]) {
                    hasNext = true;
                    visited[nextAlphabetIndex] = true;
                    dfs(nx, ny, count + 1);
                    visited[nextAlphabetIndex] = false;
                }
            }
        }

        if(!hasNext)
            result = Math.max(result, count);
    }

    private static int getIndex(char alphabet) {
        return (int)alphabet - (int)'A';
    }

    private static int result;
    private static int r, c;
    private static char[][] graph;
    private static boolean[] visited;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
}