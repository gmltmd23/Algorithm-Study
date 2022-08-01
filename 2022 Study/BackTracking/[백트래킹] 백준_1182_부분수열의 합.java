import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int N, S, result;
    private static int[] numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bufferedReader.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        result = 0;

        st = new StringTokenizer(bufferedReader.readLine(), " ");
        numbers = new int[N];
        for(int i = 0; i < N; ++i)
            numbers[i] = Integer.parseInt(st.nextToken());

        tracking(0, 0);
        System.out.println((S == 0) ? (result - 1) : (result));
    }

    public static void tracking(int depth, int nowSum) {
        if(depth == N) {
            if(nowSum == S) ++result;
            return;
        }

        tracking(depth + 1, nowSum + numbers[depth]);
        tracking(depth + 1, nowSum);
    }
}