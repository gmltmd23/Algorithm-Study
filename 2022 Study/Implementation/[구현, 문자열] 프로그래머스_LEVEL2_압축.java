import java.util.*;

public class Main {
    public static int[] solution(String msg) {
        Map<String, Integer> dictionary = new HashMap<>();
        int lastDictionaryIndex = 27;
        for(int i = 0; i < 26; ++i) {
            String alphabet = Character.toString((char)(i + 65));
            dictionary.put(alphabet, (i + 1));
        }

        ArrayList<Integer> answer = new ArrayList<>();
        int left = 0;
        while(left < msg.length()) {
            int longest = left;
            for(int right = msg.length() - 1; right > left; --right) {
                StringBuilder sb = new StringBuilder();
                for(int i = left; i <= right; ++i)
                    sb.append(msg.charAt(i));
                if(dictionary.containsKey(sb.toString())) {
                    longest = right;
                    break;
                }
            }

            StringBuilder sb = new StringBuilder();
            for(int i = left; i <= longest; ++i)
                sb.append(msg.charAt(i));
            answer.add(dictionary.get(sb.toString()));

            if(longest + 1 < msg.length()) {
                sb.append(msg.charAt(longest + 1));
                dictionary.put(sb.toString(), lastDictionaryIndex);
                ++lastDictionaryIndex;
            }

            left = longest + 1;
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        String msg = "KAKAO";
        System.out.println(solution(msg));
    }
}