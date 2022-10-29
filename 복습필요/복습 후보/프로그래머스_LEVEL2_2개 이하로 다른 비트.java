public class Main {
    private static boolean isOkayBit(long origin, long target) {
        String originBit = Long.toBinaryString(origin);
        String targetBit = Long.toBinaryString(target);

        int diffBitCount = targetBit.length() - originBit.length();
        int lastIndexOfOrigin = originBit.length() - 1;
        int lastIndexOfTarget = targetBit.length() - 1;

        while(lastIndexOfOrigin >= 0) {
            if(originBit.charAt(lastIndexOfOrigin--) != targetBit.charAt(lastIndexOfTarget--))
                ++diffBitCount;
        }

        return (diffBitCount <= 2);
    }

    private static long getLowestValue(long target) {
        if(target % 2 == 0) {
            return target + 1;
        }
        else {
            StringBuilder sb = new StringBuilder("0");
            sb.append(Long.toBinaryString(target));

            for(int i = sb.length() - 1; i >= 0; --i) {
                if(sb.charAt(i) == '0') {
                    sb.replace(i, i + 1, "1");
                    sb.replace(i + 1, i + 2, "0");
                    break;
                }
            }

            return Long.parseLong(sb.toString(), 2);
        }
    }

    private static long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        for(int i = 0; i < numbers.length; ++i)
            answer[i] = getLowestValue(numbers[i]);

        return answer;
    }

    public static void main(String[] args) {
        long[] numbers = {2, 7};
        System.out.println(solution(numbers));
    }
}