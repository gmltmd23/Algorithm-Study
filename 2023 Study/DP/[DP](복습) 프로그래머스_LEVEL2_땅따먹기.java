public class Main {
    public static int solution(int[][] land) {
        int n = land.length;
        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < 4; ++j)
                land[i][j] += Math.max(Math.max(land[i - 1][(j + 1) % 4], land[i - 1][(j + 2) % 4]), land[i - 1][(j + 3) % 4]);
        }

        int answer = 0;
        for(int i = 0; i < 4; ++i)
            answer = Math.max(answer, land[n - 1][i]);

        return answer;
    }

    public static void main(String[] args) {
        int[][] land = {{1,2,3,5}, {5,6,7,8}, {4,3,2,1}};
        System.out.println(solution(land));
    }
}