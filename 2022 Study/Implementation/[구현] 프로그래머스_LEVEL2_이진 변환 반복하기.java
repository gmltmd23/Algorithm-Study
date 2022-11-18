public class Main {
    public static int[] solution(String s) {
        int[] answer = new int[2]; // [ changedCount, zeroCount ]
        while(s.length() > 1) {
            int countOne = 0;
            for(int i = 0; i < s.length(); ++i) {
                if(s.charAt(i) == '0')
                    ++answer[1];
                else
                    ++countOne;
            }

            s = Integer.toBinaryString(countOne);
            ++answer[0];
        }

        return answer;
    }

    public static void main(String[] args) {
        String s = "110010101001";
        System.out.println(solution(s));
    }
}