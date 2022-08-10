import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; ++i)
            numbers[i] = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(br.readLine());

        int left = 0;
        int right = n - 1;
        int result = 0;

        Arrays.sort(numbers);
        while(left < right) {
            int total = numbers[left] + numbers[right];
            if(total == x)
                ++result;

            if(total < x)
                ++left;
            else
                --right;
        }

        System.out.println(result);
    }
}