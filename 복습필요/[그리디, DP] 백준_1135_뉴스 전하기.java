import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
    public int parent = -1;
    public int index = 0;
    public LinkedList<Node> childList = new LinkedList<>();

    @Override
    public int compareTo(Node o) {
        return o.childList.size() - this.childList.size(); // 내림차순 정렬
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        nodeList = new Node[n];

        for(int i = 0; i < n; ++i) {
            nodeList[i] = new Node();
            Node nowNode = nodeList[i];

            nowNode.index = i;
            nowNode.parent = Integer.parseInt(st.nextToken());
            if(nowNode.parent != -1)
                nodeList[nowNode.parent].childList.add(nowNode);
        }

        process(0, 0);
        System.out.println(result);
    }

    private static void process(int nodeIndex, int count) {
        Node nowNode = nodeList[nodeIndex];
        result = Math.max(result, count);
        if(nowNode.childList.size() == 0)
            return;

        Collections.sort(nowNode.childList);
        int addSecond = 1;
        for(Node nextNode : nowNode.childList)
            process(nextNode.index, count + addSecond++);
    }

    private static int result = 0;
    private static Node[] nodeList;
}