public class Main {
    private static boolean[] visited;
    private static int fatigue;
    private static int answer;

    public static void backTrakcing(int[][] dungeons, int count) {
        answer = Math.max(answer, count);
        for(int i = 0; i < dungeons.length; ++i){
            if(!visited[i] && fatigue >= dungeons[i][0]) {
                visited[i] = true;
                fatigue -= dungeons[i][1];
                backTrakcing(dungeons, count + 1);
                fatigue += dungeons[i][1];
                visited[i] = false;
            }
        }
    }

    public static int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        fatigue = k;
        answer = 0;
        backTrakcing(dungeons, 0);
        return answer;
    }

    public static void main(String[] args) {
        int k = 80;
        int[][] dungeons = {{80, 20}, {50, 40}, {30, 10}};
        System.out.println(solution(k, dungeons));
    }
}