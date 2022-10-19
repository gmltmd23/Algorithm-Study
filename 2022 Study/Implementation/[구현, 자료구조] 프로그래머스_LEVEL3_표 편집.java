import java.util.*;

public class Main {

    static class Node {
        int pre, cur, next;

        public Node(int pre, int cur, int next) {
            this.pre = pre;
            this.cur = cur;
            this.next = next;
        }
    }
    private static String solution(int n, int k, String[] cmd) {
        int[] pre = new int[n];
        int[] next = new int[n];
        for(int i = 0; i < n; i++) {
            pre[i] = i - 1;
            next[i] = i + 1;
        }
        next[n - 1] = -1;

        Stack<Node> stack = new Stack<>();
        StringBuilder sb = new StringBuilder("0".repeat(n));
        for(int i = 0; i < cmd.length; i++) {
            char c = cmd[i].charAt(0);
            if(c == 'U') {
                int num = Integer.valueOf(cmd[i].substring(2));
                while(num-- > 0) {
                    k = pre[k];
                }
            } else if(c == 'D') {
                int num = Integer.valueOf(cmd[i].substring(2));
                while(num-- > 0) {
                    k = next[k];
                }
            } else if(c == 'C') {
                stack.push(new Node(pre[k], k, next[k]));
                if(pre[k] != -1) next[pre[k]] = next[k]; //현재 노드 삭제 후 앞뒤 연결
                if(next[k] != -1) pre[next[k]] = pre[k];
                sb.setCharAt(k, 'X');

                if(next[k] != -1) k = next[k];
                else k = pre[k]; //마지막 행인 경우에 바로 윗 행 선택
            } else {
                Node node = stack.pop();
                if(node.pre != -1) next[node.pre] = node.cur; //연결 정보 복구
                if(node.next != -1) pre[node.next] = node.cur;
                sb.setCharAt(node.cur, 'O');
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        int n = 8;
        int k = 2;
        String[] cmd = {"D 2","C","U 3","C","D 4","C","U 2","Z","Z"};
        System.out.println(solution(n, k, cmd));
    }
}