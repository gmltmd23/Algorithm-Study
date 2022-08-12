import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int leftMileage = Integer.parseInt(st.nextToken());
        subjectCandidateQueue = new PriorityQueue<>();

        for(int subjectCount = 0; subjectCount < n; ++subjectCount) {
            st = new StringTokenizer(br.readLine());
            int applyPersonCount = Integer.parseInt(st.nextToken());
            int limitPersonCount = Integer.parseInt(st.nextToken());

            PriorityQueue<Integer> appliedPersonQueue = new PriorityQueue<>();
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens())
                appliedPersonQueue.offer(Integer.parseInt(st.nextToken()));

            int diff = applyPersonCount - limitPersonCount;
            if(diff < 0) {
                subjectCandidateQueue.offer(1);
            }
            else {
                for(int i = 0; i < diff; ++i)
                    appliedPersonQueue.poll();
                subjectCandidateQueue.offer(appliedPersonQueue.peek());
            }
        }

        int result = 0;
        while(!subjectCandidateQueue.isEmpty() && leftMileage >= subjectCandidateQueue.peek()) {
            ++result;
            leftMileage -= subjectCandidateQueue.poll();
        }

        System.out.print(result + "\n");
    }

    private static PriorityQueue<Integer> subjectCandidateQueue;
}