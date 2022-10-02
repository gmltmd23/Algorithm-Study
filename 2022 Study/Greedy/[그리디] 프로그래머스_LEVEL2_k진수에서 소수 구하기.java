public class Main {
    public static boolean isPrimeNumber(long candidate) {
        if(candidate == 1)
            return false;

        for(long i = 2; i <= (long)Math.sqrt(candidate); ++i) {
            if(candidate % i == 0)
                return false;
        }

        return true;
    }
    public static int solution(int n, int k) {
        int answer = 0;
        String kNumber = Integer.toString(n, k);
        for(String element : kNumber.split("0")) {
            if(element.isEmpty())
                continue;
            long candidate = Long.parseLong(element);
            if(isPrimeNumber(candidate))
                ++answer;
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 437674;
        int k = 3;

        System.out.println(solution(n, k));
    }
}