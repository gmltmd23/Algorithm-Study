public class Main {
    public static int solution(int[] stones, int k) {
        int maxValue = 200000000;
        int minValue = 1;
        int midValue;
        int answer = 0;

        while(minValue <= maxValue) {
            midValue = (minValue + maxValue) / 2;
            int zeroStoneCount = 0;
            boolean isCross = true;

            for(int stone : stones) {
                if(stone <= midValue)
                    ++zeroStoneCount;
                else
                    zeroStoneCount = 0;

                if(zeroStoneCount == k) {
                    isCross = false;
                    break;
                }
            }

            if(isCross) {
                minValue = midValue + 1;
                answer = Math.max(answer, midValue);
            }
            else {
                maxValue = midValue - 1;
            }
        }

        return answer + 1;
    }

    public static void main(String[] args) {
        int[] stones = {2, 4, 5, 3, 2, 1, 4, 2, 5, 1};
        int k = 3;
        System.out.println(solution(stones, k));
    }
}