import java.util.*;

public class Main {
    static class Job implements Comparable<Job> {
        public int requestTime;
        public int burstTime;

        public Job(int requestTime, int burstTime) {
            this.requestTime = requestTime;
            this.burstTime = burstTime;
        }

        @Override
        public int compareTo(Job otherJob) {
            return this.burstTime - otherJob.burstTime;
        }
    }

    public static int solution(int[][] jobs) {
        ArrayList<Job> jobList = new ArrayList<>();
        for(int[] element : jobs)
            jobList.add(new Job(element[0], element[1]));
        Collections.sort(jobList, Comparator.comparingInt(o -> o.requestTime));

        int nowTime = 0;
        int totalTime = 0;
        int index = 0;
        int count = 0;

        PriorityQueue<Job> waitJobQueue = new PriorityQueue<>();
        while(count < jobList.size()) {
            while(index < jobList.size() && jobList.get(index).requestTime <= nowTime) {
                waitJobQueue.add(jobList.get(index));
                ++index;
            }

            if(waitJobQueue.isEmpty()) {
                nowTime = jobList.get(index).requestTime;
            }
            else {
                Job job = waitJobQueue.poll();
                totalTime += (nowTime - job.requestTime) + job.burstTime;
                nowTime += job.burstTime;
                ++count;
            }
        }

        return totalTime / jobList.size();
    }

    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        //int[][] jobs = {{15, 3}};
        //int[][] jobs = {{0, 16}, {0, 14}, {15, 1}, {13, 13}};
        System.out.println(solution(jobs));
    }
}