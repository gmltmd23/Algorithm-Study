import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Locale;

public class Main {
    public static int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if(cacheSize == 0)
            return cities.length * 5;

        Deque<String> q = new LinkedList<>();
        HashSet<String> checkSet = new HashSet<>();
        for(String city : cities) {
            city = city.toLowerCase(Locale.ROOT);
            if(checkSet.contains(city)) {
                ++answer;
                if(q.peekLast() != city) {
                    q.remove(city);
                    q.offer(city);
                }
            }
            else {
                answer += 5;
                if(cacheSize > 0)
                    --cacheSize;
                else
                    checkSet.remove(q.pollFirst());

                checkSet.add(city);
                q.offer(city);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int cacheSize = 0;
        String[] cities = {"LA", "LA"};
        System.out.println(solution(cacheSize, cities));
    }
}