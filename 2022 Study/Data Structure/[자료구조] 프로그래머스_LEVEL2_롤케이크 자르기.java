import java.util.*;

public class Main {
    public static int solution(int[] topping) {
        HashSet<Integer> wholeKindSet = new HashSet<>();
        int[] brotherArray = new int[10001];
        for(int eachTopping : topping) {
            wholeKindSet.add(eachTopping);
            ++brotherArray[eachTopping];
        }

        int answer = 0;
        HashSet<Integer> cheolsuSet = new HashSet<>();
        for(int eachTopping : topping) {
            cheolsuSet.add(eachTopping);
            --brotherArray[eachTopping];
            if(brotherArray[eachTopping] <= 0)
                wholeKindSet.remove(eachTopping);

            if(wholeKindSet.size() == cheolsuSet.size())
                ++answer;
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] toping = {1, 2, 3, 3, 3};
        System.out.println(solution(toping));
    }
}