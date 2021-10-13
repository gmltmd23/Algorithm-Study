/*
*
* 백준 문제 11000번 그리디_강의실 배정
*
* 파이썬으로 풀었던것을 자바로도 풀어보았다.
* 람다, sort, PriorityQueue를 연습하는데 도움이되는 좋은 문제였다.
*
* */

import java.util.*;
import java.io.*;

class Time {
    int start;
    int end;

    public Time(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int n = Integer.parseInt(br.readLine());
        Time[] time = new Time[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            time[i] = new Time(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(time, (Time t1, Time t2) -> t1.start == t2.start ? t1.end - t2.end : t1.start - t2.start);

        PriorityQueue<Integer> room = new PriorityQueue<>();
        room.offer(time[0].end);
        for (int i = 1; i < n; i++) {
            if (time[i].start >= room.peek())
                room.poll();
            room.offer(time[i].end);
        }

        System.out.println(room.size());
    }
}