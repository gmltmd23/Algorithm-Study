import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] aArray = new int[n];
        int[] bArray = new int[m];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; ++i)
            aArray[i] = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; ++i)
            bArray[i] = Integer.parseInt(st.nextToken());

        int indexOfA = 0;
        int indexOfB = 0;
        StringBuilder sb = new StringBuilder();
        while(indexOfA < aArray.length && indexOfB < bArray.length) {
            if(aArray[indexOfA] <= bArray[indexOfB])
                sb.append(aArray[indexOfA++] + " ");
            else
                sb.append(bArray[indexOfB++] + " ");
        }

        while(indexOfA < aArray.length)
            sb.append(aArray[indexOfA++] + " ");

        while(indexOfB < bArray.length)
            sb.append(bArray[indexOfB++] + " ");

        System.out.println(sb);

        br.close();
    }
}