public class Main {
    public static int solution(String s) {
        int answer = 1;
        int len = s.length();
        for(int left = 0; left < len - 1; ++left) {
            StringBuilder sb = new StringBuilder();
            sb.append(s.charAt(left));
            for(int right = left + 1; right < len; ++right) {
                sb.append(s.charAt(right));
                int sbLength = sb.length();
                if(sbLength < answer)
                    continue;

                boolean isSameString = true;
                for(int i = 0; i < sb.length(); ++i) {
                    if(sb.charAt(i) != sb.charAt(sbLength - 1 - i)) {
                        isSameString = false;
                        break;
                    }
                }

                if(isSameString)
                    answer = Math.max(answer, sbLength);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String s = "abacde";
        System.out.println(solution(s));
    }
}