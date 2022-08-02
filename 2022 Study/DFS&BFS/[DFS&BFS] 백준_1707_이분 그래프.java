import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        StringTokenizer st = null;
        for(int testCase = 0; testCase < K; ++testCase) {
            st = new StringTokenizer(br.readLine(), " ");
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            colors = new boolean[V + 1];
            visited = new boolean[V + 1];
            graph = new ArrayList[V + 1];
            for(int i = 1; i < V + 1; ++i)
                graph[i] = new ArrayList<>();

            for(int i = 0; i < E; ++i) {
                st = new StringTokenizer(br.readLine(), " ");
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                graph[b].add(a);
            }

            boolean isBipartiteGraph = true;
            for(int i = 1; i < (V + 1); ++i) {
                if(!visited[i]) {
                    isBipartiteGraph = bfsAndCheckBipartiteGraph(i);
                    if(!isBipartiteGraph) break;
                }
            }

            System.out.println((isBipartiteGraph) ? "YES" : "NO");
        }
    }

    public static boolean bfsAndCheckBipartiteGraph(int startNode) {
        Queue<Integer> q = new LinkedList<>();
        visited[startNode] = true;
        q.offer(startNode);

        while(!q.isEmpty()) {
            int node = q.poll();
            for(int nextNode : graph[node]) {
                if(!visited[nextNode]) {
                    visited[nextNode] = true;
                    colors[nextNode] = !colors[node];
                    q.offer(nextNode);
                }
                else {
                    if(colors[nextNode] == colors[node])
                        return false;
                }
            }
        }

        return true;
    }

    private static ArrayList<Integer>[] graph = null;
    private static boolean[] colors, visited;
}