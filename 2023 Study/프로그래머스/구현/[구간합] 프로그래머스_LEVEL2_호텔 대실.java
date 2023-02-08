import java.util.*;

public class Main {
    private static int solution(String[][] book_time) {
        int[] minutes = new int[1500];
        for(String[] eachBookTime : book_time) {
            String start = eachBookTime[0];
            String end = eachBookTime[1];
            StringTokenizer startToken = new StringTokenizer(start, ":");
            StringTokenizer endToken = new StringTokenizer(end, ":");

            int startMinute = (Integer.parseInt(startToken.nextToken()) * 60) + Integer.parseInt(startToken.nextToken());
            int endMinute = (Integer.parseInt(endToken.nextToken()) * 60) + Integer.parseInt(endToken.nextToken());
            endMinute += 10;

            minutes[startMinute] += 1;
            minutes[endMinute] -= 1;
        }

        int answer = minutes[0];
        for(int i = 0; i < minutes.length - 1; ++i) {
            minutes[i + 1] += minutes[i];
            answer = Math.max(answer, minutes[i + 1]);
        }

        return answer;
    }

    public static void main(String[] args) {
        String[][] book_time = {{"09:10", "10:10"}, {"10:20", "12:20"}};
        System.out.println(solution(book_time));
    }
}