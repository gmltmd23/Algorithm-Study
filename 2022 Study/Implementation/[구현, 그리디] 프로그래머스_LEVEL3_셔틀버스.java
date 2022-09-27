import java.util.*;

public class Main {

    public static String makeTimeString(int hour, int minute) {
        StringBuilder time = new StringBuilder();
        time.append((hour < 10) ? "0" + hour : hour);
        time.append(":");
        time.append((minute < 10) ? "0" + minute : minute);

        return time.toString();
    }

    public static String addTime(String nowTime, int adder) {
        String[] splitedTime = nowTime.split(":");
        int nowHour = Integer.parseInt(splitedTime[0]);
        int nowMinutes = Integer.parseInt(splitedTime[1]);
        nowMinutes += adder;
        if(nowMinutes >= 60) {
            nowMinutes -= 60;
            ++nowHour;
        }
        else if(nowMinutes < 0) {
            nowMinutes = 60 + nowMinutes;
            --nowHour;
        }

        return makeTimeString(nowHour, nowMinutes);
    }
    public static String solution(int n, int t, int m, String[] timetable) {
        Arrays.sort(timetable);
        Deque<String> q = new ArrayDeque<>();
        for(String element : timetable)
            q.offer(element);

        String nowTime = "09:00";
        for(int round = 0; round < n; ++round) {
            int leftCount = m;
            String maxTime = null;
            while(!q.isEmpty() && leftCount != 0) {
                maxTime = q.peekFirst();
                if(maxTime.compareTo(nowTime) > 0) {
                    if(round < (n - 1))
                        break;
                    return nowTime;
                }
                else{
                    --leftCount;
                    q.pollFirst();
                }
            }

            if(leftCount == 0) {
                if(round >= (n - 1))
                    return addTime(maxTime, -1);
            }
            else if(q.isEmpty()) {
                return nowTime;
            }

            nowTime = addTime(nowTime, t);
        }

        return nowTime;
    }

    public static void main(String[] args) {
        int n = 10;
        int t = 25;
        int m = 1;
        String[] timetable = {"09:00", "09:10" ,"09:20" ,"09:30" ,"09:40" ,"09:50",
                "10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50"};
        System.out.println(solution(n, t, m, timetable));
    }
}