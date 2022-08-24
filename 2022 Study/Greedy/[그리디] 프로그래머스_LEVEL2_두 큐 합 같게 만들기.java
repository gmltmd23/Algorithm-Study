import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static int solution(int[] queue1, int[] queue2) {
        Deque<Integer> deque1 = new ArrayDeque<>();
        Deque<Integer> deque2 = new ArrayDeque<>();

        long totalOfQueue1 = 0;
        long totalOfQueue2 = 0;
        int maxOfQueue1 = 0;
        int maxOfQueue2 = 0;

        for(int i = 0; i < queue1.length; ++i) {
            deque1.offer(queue1[i]);
            maxOfQueue1 = Math.max(maxOfQueue1, queue1[i]);
            totalOfQueue1 += queue1[i];

            deque2.offer(queue2[i]);
            maxOfQueue2 = Math.max(maxOfQueue2, queue2[i]);
            totalOfQueue2 += queue2[i];
        }

        int count = 0;
        while(totalOfQueue1 != totalOfQueue2) {
            ++count;
            if(totalOfQueue1 > totalOfQueue2) {
                int data = deque1.pollFirst();
                totalOfQueue1 -= data;
                totalOfQueue2 += data;
                deque2.offer(data);
            }
            else {
                int data = deque2.pollFirst();
                totalOfQueue2 -= data;
                totalOfQueue1 += data;
                deque1.offer(data);
            }

            if(count > (queue1.length + queue2.length) * 2)
                return -1;
        }

        return count;
    }

    public static void main(String[] args) {
        int[] queue1 = {1, 1, 1, 8, 10, 9};
        int[] queue2 = {1, 1, 1, 1, 1, 1};
        System.out.println(solution(queue1, queue2));
    }
}