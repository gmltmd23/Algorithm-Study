/*
*
* 백준 문제 1922번 그래프 탐색_네트워크 연결
*
* 아까 파이썬으로 풀었던것을 자바로 코드화 시켜봤다.
* 파이썬으로 짤때는 Edge같은 클래스를 안만들어도 되서 편한데ㅋㅋㅋㅋㅋㅋ
* 파이썬 쓰다보니깐 자바 코드 왜이렇게 길어보이냐 연습하자
*
* */

import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
    int start, end, cost;

    Edge(int a, int b, int c) {
        this.start = a;
        this.end = b;
        this.cost = c;
    }

    @Override
    public int compareTo(Edge obj) {
        return this.cost - obj.cost;
    }
}

class Main {
    static int n, m;
    static int[] parents;
    static ArrayList<Edge> edges;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = null;
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        parents = new int[n + 1];
        for (int i = 1; i < parents.length; i++)
            parents[i] = i;

        edges = new ArrayList<Edge>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            edges.add(new Edge(a, b, c));
        }
        Collections.sort(edges);

        long answer = 0;
        for (Edge edge : edges) {
            if (find_parents(parents, edge.start) != find_parents(parents, edge.end)) {
                union_parents(parents, edge.start, edge.end);
                answer += edge.cost;
            }
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    static int find_parents(int[] parents, int x) {
        if (parents[x] != x)
            parents[x] = find_parents(parents, parents[x]);
        return parents[x];
    }

    static void union_parents(int[] parents, int a, int b) {
        a = find_parents(parents, a);
        b = find_parents(parents, b);
        if (a < b)
            parents[b] = a;
        else
            parents[a] = b;
    }
}