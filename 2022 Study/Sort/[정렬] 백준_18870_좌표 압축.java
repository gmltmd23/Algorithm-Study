import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] originalArray = new int[n];
        int[] sortedArray = new int[n];
        HashMap<Integer, Integer> rankingMap = new HashMap<>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; ++i)
            sortedArray[i] = originalArray[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(sortedArray);
        int rank = 0;
        for(int element : sortedArray) {
            if(!rankingMap.containsKey(element))
                rankingMap.put(element, rank++);
        }

        StringBuilder stringBuilder = new StringBuilder();
        for(int key : originalArray) {
            int ranking = rankingMap.get(key);
            stringBuilder.append(ranking).append(' ');
        }

        System.out.println(stringBuilder);
    }
}