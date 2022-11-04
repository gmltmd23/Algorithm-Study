import javax.swing.plaf.InsetsUIResource;
import java.util.HashMap;

public class Main {
    public static boolean isPerfectDay(int[] number, int[] cmpArray) {
        for(int i = 0; i < number.length; ++i) {
            if(number[i] != cmpArray[i])
                return false;
        }
        return true;
    }

    public static int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> indexMap = new HashMap<>();
        int totalCount = 0;
        for(int i = 0; i < want.length; ++i) {
            totalCount += number[i];
            indexMap.put(want[i], i);
        }

        int answer = 0;
        for(int left = 0; left <= (discount.length - totalCount); ++left) {
            int right = left + totalCount;
            if(indexMap.containsKey(discount[left])) {
                int[] cmpArray = new int[indexMap.size()];
                for(int i = left; i < right; ++i) {
                    if(!indexMap.containsKey(discount[i]))
                        break;
                    ++cmpArray[indexMap.get(discount[i])];
                }

                if(isPerfectDay(number, cmpArray))
                    ++answer;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] want = {"banana", "apple", "rice", "pork", "pot"};
        int[] number = {3, 2, 2, 2, 1};
        String[] discount = {"chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"};
        System.out.println(solution(want, number, discount));
    }
}