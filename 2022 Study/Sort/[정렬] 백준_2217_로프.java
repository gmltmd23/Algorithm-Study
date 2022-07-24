import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] ropes = new int[n];
        for(int i = 0; i < n; ++i)
            ropes[i] = Integer.parseInt(br.readLine());

        Arrays.sort(ropes);
        int result = 0;
        for(int i = 0; i < n; ++i)
            result = Math.max(result, ropes[i] * (n - i));

        System.out.print(result);
    }
}