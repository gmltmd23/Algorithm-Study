import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        relations = new boolean[n + 1][n + 1];
        for(int i = 0; i < k; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            relations[a][b] = true;
        }

        floyd();

        int s = Integer.parseInt(br.readLine());
        StringBuilder stringBuilder = new StringBuilder();
        for(int i = 0; i < s; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            judgeResult(a, b, stringBuilder);
        }

        System.out.print(stringBuilder.toString());
    }

    private static void floyd() {
        for(int k = 0; k < n + 1; ++k) {
            for(int a = 0; a < n + 1; ++a) {
                for(int b = 0; b < n + 1; ++b) {
                    if(relations[a][k] && relations[k][b])
                        relations[a][b] = true;
                }
            }
        }
    }

    private static void judgeResult(final int a, final int b, StringBuilder stringBuilder) {
        if(relations[a][b])
            stringBuilder.append(-1 + "\n");
        else if(relations[b][a])
            stringBuilder.append(1 + "\n");
        else
            stringBuilder.append(0 + "\n");
    }

    private static int n, k;
    private static boolean[][] relations;
}