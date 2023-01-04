import java.util.*;

public class Main {
    public static int findParent(int[] parents, int x) {
        if(parents[x] != x)
            parents[x] = findParent(parents, parents[x]);
        return parents[x];
    }

    public static void unionParent(int[] parents, int a, int b) {
        a = findParent(parents, a);
        b = findParent(parents, b);
        if(a < b)
            parents[b] = a;
        else
            parents[a] = b;
    }

    public static int solution(int n, int[][] costs) {
        int[] parents = new int[n];
        for(int i = 0; i < parents.length; ++i)
            parents[i] = i;

        int answer = 0;
        Arrays.sort(costs, Comparator.comparingInt(o -> o[2]));
        for(int[] element : costs) {
            int start = element[0];
            int end = element[1];
            int cost = element[2];

            if(findParent(parents, start) != findParent(parents, end)) {
                answer += cost;
                unionParent(parents, start, end);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 4;
        int[][] costs = {{0, 1, 1}, {0, 2, 2}, {1, 2, 5}, {1, 3, 1}, {2, 3, 8}};
        System.out.println(solution(n, costs));
    }
}