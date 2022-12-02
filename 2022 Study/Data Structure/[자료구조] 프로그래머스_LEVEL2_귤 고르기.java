import java.util.*;

public class Main {
    static class TangerineKind implements Comparable {
        public int kind;
        public int count;

        public TangerineKind(int kind, int count) {
            this.kind = kind;
            this.count = count;
        }

        @Override
        public int compareTo(Object o) {
            TangerineKind otherTangerineKind = (TangerineKind) o;
            return (this.count - otherTangerineKind.count);
        }
    }

    public static int solution(int k, int[] tangerine) {
        HashMap<Integer, Integer> tangerineMap = new HashMap<>();
        int tangerineTotal = 0;
        for(int eachTangerine :tangerine) {
            if(!tangerineMap.containsKey(eachTangerine))
                tangerineMap.put(eachTangerine, 0);
            tangerineMap.put(eachTangerine, tangerineMap.get(eachTangerine) + 1);
            ++tangerineTotal;
        }

        PriorityQueue<TangerineKind> tangerineQueue = new PriorityQueue<>();
        for(Integer kind : tangerineMap.keySet())
            tangerineQueue.offer(new TangerineKind(kind, tangerineMap.get(kind)));

        while(!tangerineQueue.isEmpty()) {
            TangerineKind nowTangerine = tangerineQueue.poll();
            if((tangerineTotal - nowTangerine.count) >= k) {
                tangerineTotal -= nowTangerine.count;
            }
            else {
                tangerineQueue.offer(nowTangerine);
                break;
            }
        }

        return tangerineQueue.size();
    }

    public static void main(String[] args) {
        int k = 4;
        int[] tangerine = {1, 3, 2, 5, 4, 5, 2, 3};
        System.out.println(solution(k, tangerine));
    }
}