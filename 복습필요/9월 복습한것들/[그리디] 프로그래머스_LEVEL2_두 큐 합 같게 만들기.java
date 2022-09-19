import java.util.*;

public class Main {
    private static int solution(int[] queue1, int[] queue2) {
        Deque<Integer> firstQueue = new ArrayDeque<>();
        Deque<Integer> secondQueue = new ArrayDeque<>();

        long firstSum = 0;
        for(int element : queue1) {
            firstSum += element;
            firstQueue.offer(element);
        }

        long secondSum = 0;
        for(int element : queue2) {
            secondSum += element;
            secondQueue.offer(element);
        }

        int allQueueSize = queue1.length * 2;
        int count = 0;
        while(count <= allQueueSize * 2) {
            if(firstSum > secondSum) {
                secondQueue.offer(firstQueue.pollFirst());
                firstSum -= secondQueue.peekLast();
                secondSum += secondQueue.peekLast();
            }
            else if(firstSum < secondSum) {
                firstQueue.offer(secondQueue.pollFirst());
                secondSum -= firstQueue.peekLast();
                firstSum += firstQueue.peekLast();
            }
            else
                return count;

            ++count;
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] queue1 = { 1,1,1,1,1 };
        int[] queue2 = { 1,1,1,9,1 };

        System.out.print(solution(queue1, queue2));
    }
}