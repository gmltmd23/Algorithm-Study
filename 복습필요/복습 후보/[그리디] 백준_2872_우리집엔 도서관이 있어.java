import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] books = new int[n];
        for(int i = 0; i < n; ++i)
            books[i] = Integer.parseInt(br.readLine());
        int maxBook = n;

        int result = 0;
        for(int i = n - 1; i >= 0; --i) {
            if(maxBook == books[i])
                --maxBook;
            else
                ++result;
        }

        System.out.println(result);
        br.close();
    }
}