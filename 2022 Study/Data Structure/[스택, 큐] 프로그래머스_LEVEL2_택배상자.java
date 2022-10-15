import java.util.*;

public class Main {
    private static int solution(int[] order) {
        Queue<Integer> mainBelt = new LinkedList();
        Stack<Integer> subBelt = new Stack();
        for(int i = 1; i <= order.length; ++i)
            mainBelt.offer(i);

        int answer = 0;
        for(int nowOrder : order) {
            while(!mainBelt.isEmpty() && mainBelt.peek() <= nowOrder)
                subBelt.push(mainBelt.poll());

            if(subBelt.peek() == nowOrder) {
                subBelt.pop();
                ++answer;
            }
            else {
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] order = {4, 3, 1, 2, 5};
        System.out.println(solution(order));
    }
}