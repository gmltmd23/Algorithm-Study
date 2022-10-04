public class Main {
    public static int solution(int n, int[] stations, int w) {
        int answer = 0;
        int start = 1;
        int supportCoverage = (2 * w) + 1;

        for(int station : stations) {
           int left = station - w - 1;
           if(left > 0 && (start <= left)) {
               int needCoverage = (left - start) + 1;
               answer += needCoverage / supportCoverage;
               if(needCoverage % supportCoverage > 0)
                   answer += 1;
           }
           start = station + w + 1;
        }

        if(start <= n) {
            int needCoverage = (n - start) + 1;
            answer += needCoverage / supportCoverage;
            if(needCoverage % supportCoverage > 0)
                answer += 1;
        }

        return answer;
    }

    public static void main(String[] args) {
        int N = 16;
        int[] stations = {9};
        int W = 2;
        System.out.println(solution(N, stations, W));
    }
}