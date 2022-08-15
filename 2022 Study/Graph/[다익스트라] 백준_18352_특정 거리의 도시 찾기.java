import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class CityAndCost {
    public CityAndCost(final int city, final int cost) {
        this.city = city;
        this.cost = cost;
    }

    public int city;
    public int cost;
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        distance = new int[n + 1];
        Arrays.fill(distance, INF);
        graph = new LinkedList[n + 1];
        for(int i = 1; i < n + 1; ++i)
            graph[i] = new LinkedList<>();

        for(int i = 0; i < m; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        dijkstra(x);

        boolean hasK = false;
        for(int i = 1; i < n + 1; ++i) {
            if(distance[i] == k) {
                hasK = true;
                System.out.print(i + "\n");
            }
        }

        if(!hasK)
            System.out.println(-1);
    }

    private static void dijkstra(int start) {
        distance[start] = 0;
        Queue<CityAndCost> q = new LinkedList<>();
        q.offer(new CityAndCost(start, 0));

        while(!q.isEmpty()) {
            CityAndCost cityAndCost = q.poll();
            final int nowCity = cityAndCost.city;
            final int nowCost = cityAndCost.cost;
            if(distance[nowCity] < nowCost)
                continue;

            for(final int nextCity : graph[nowCity]) {
                int nextCost = nowCost + ONE;
                if(nextCost < distance[nextCity]) {
                    distance[nextCity] = nextCost;
                    q.offer(new CityAndCost(nextCity, nextCost));
                }
            }
        }
    }

    private static final int ONE = 1;
    private static final int INF = Integer.MAX_VALUE;
    private static int[] distance;
    private static LinkedList<Integer>[] graph;
}