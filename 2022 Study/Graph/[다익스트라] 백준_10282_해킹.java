import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class NextComputer implements Comparable<NextComputer> {
    public NextComputer(int next, int time) {
        this.next = next;
        this.time = time;
    }

    public int next;
    public int time;

    @Override
    public int compareTo(NextComputer o) {
        return this.time - o.time;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st = null;
        for(int testCase = 0; testCase < T; ++testCase) {
            st = new StringTokenizer(br.readLine(), " ");
            int n = Integer.parseInt(st.nextToken()); // 컴퓨터 대수
            int d = Integer.parseInt(st.nextToken()); // 의존성 개수
            int c = Integer.parseInt(st.nextToken()); // 해킹당한 컴퓨터의 번호

            graph = new HashMap<>();
            distance = new int[n + 1];
            Arrays.fill(distance, Integer.MAX_VALUE);

            for(int i = 0; i < d; ++i) {
                st = new StringTokenizer(br.readLine(), " ");
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());

                if(!graph.containsKey(b))
                    graph.put(b, new LinkedList<>());
                graph.get(b).add(new NextComputer(a, s));
            }

            dijkstra(c);
            int computerCount = 0;
            int maximumTime = 0;
            for(int i = 1; i < n + 1; ++i) {
                if(distance[i] != Integer.MAX_VALUE) {
                    ++computerCount;
                    maximumTime = Math.max(maximumTime, distance[i]);
                }
            }
            System.out.println(computerCount + " " + maximumTime);
        }
    }

    public static void dijkstra(int startComputer) {
        distance[startComputer] = 0;
        PriorityQueue<NextComputer> q = new PriorityQueue<>();
        q.offer(new NextComputer(startComputer, 0));

        while(!q.isEmpty()) {
            NextComputer nextComputer = q.poll();
            int computer = nextComputer.next;
            int time = nextComputer.time;
            if(distance[computer] < time)
                continue;
            if(!graph.containsKey(computer))
                continue;

            for(NextComputer element : graph.get(computer)) {
                int nextTime = time + element.time;
                if(nextTime < distance[element.next]) {
                    distance[element.next] = nextTime;
                    q.offer(new NextComputer(element.next, nextTime));
                }
            }
        }
    }

    private static int[] distance;
    private static HashMap<Integer, LinkedList<NextComputer>> graph;
}