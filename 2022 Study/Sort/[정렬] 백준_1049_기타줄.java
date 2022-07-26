import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] bundle = new int[M];
        int[] single = new int[M];
        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            bundle[i] = Integer.parseInt(st.nextToken());
            single[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(bundle);
        Arrays.sort(single);

        int minBundle = bundle[0];
        for(int s : single) {
            if(minBundle > (s*6))
                minBundle = s*6;
        }

        int pack = (N/6 + 1) * minBundle;
        int sing = (N/6) * minBundle + (N%6) * single[0];

        if(pack < sing)
            System.out.println(pack);
        else
            System.out.println(sing);
    }
}