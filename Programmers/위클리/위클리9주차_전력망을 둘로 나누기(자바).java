public class Solution {
    static int find_parent(int[] parents, int x) {
        if (parents[x] != x)
            parents[x] = find_parent(parents, parents[x]);
        return parents[x];
    }

    static void union(int[] parents, int a, int b) {
        a = find_parent(parents, a);
        b = find_parent(parents, b);
        if (a < b)
            parents[b] = a;
        else
            parents[a] = b;
    }

    public int solution(int n, int[][] wires) {
        int answer = 9876543;
        for (int i = 0; i < wires.length; i++) {
            int[] parents = new int[n + 1];
            for (int idx = 0; idx < n + 1; idx++)
                parents[idx] = idx;

            for (int j = 0; j < wires.length; j++) {
                if (i == j)
                    continue;
                union(parents, wires[j][0], wires[j][1]);
            }

            int sub = 0;
            for (int k = 1; k < parents.length; k++) {
                find_parent(parents, k);
                if (parents[k] == 1)
                    sub++;
            }

            answer = Math.min(answer, Math.abs((n - sub) - sub));
        }

        return answer;
    }
}
