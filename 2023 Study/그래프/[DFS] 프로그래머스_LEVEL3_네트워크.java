public class Main {
    private static boolean[] visited;

    private static void dfs(int start, int[][] computers) {
        visited[start] = true;
        for(int i = 0; i < computers.length; ++i) {
            if(computers[start][i] == 1 && !visited[i]) {
                visited[i] = true;
                dfs(i, computers);
            }
        }
    }

    public static int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        for(int i = 0; i < n; ++i) {
            if(!visited[i]) {
                ++answer;
                dfs(i, computers);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] computers = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};
        System.out.println(solution(n, computers));
    }
}