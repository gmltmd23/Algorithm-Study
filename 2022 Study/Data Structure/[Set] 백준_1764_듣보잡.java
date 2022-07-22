import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<String> cantHearSet = new HashSet<>();
        HashSet<String> cantWatchSet = new HashSet<>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for(int i = 0; i < n; ++i)
            cantHearSet.add(br.readLine());

        for(int i = 0; i < m; ++i)
            cantWatchSet.add(br.readLine());

        cantHearSet.retainAll(cantWatchSet);
        ArrayList<String> result = (ArrayList<String>)cantHearSet.stream().collect(Collectors.toList());
        Collections.sort(result);

        System.out.println(result.size());
        for(String element : result)
            System.out.println(element);
    }
}