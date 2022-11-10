public class Main {
    private static int[] result = {-1};
    private static int finalLionScore = -1;

    private static void dfs(final int limit, int count, final int[] apeachInfo, int[] lionInfo) {
        if(limit == count) {
            int apeachScore = 0;
            int lionScore = 0;
            for(int i = 0; i < 11; ++i) {
                if(apeachInfo[i] + lionInfo[i] == 0)
                    continue;

                if(apeachInfo[i] >= lionInfo[i])
                    apeachScore += (10 - i);
                else
                    lionScore += (10 - i);
            }

            if(lionScore > apeachScore) {
                if(lionScore > finalLionScore) {
                    result = lionInfo.clone();
                    finalLionScore = lionScore;
                }
                else if(lionScore == finalLionScore) {
                    int lionSmallCount = 0;
                    int finalLionSmallCount = 0;
                    for(int i = 10; i >= 0; --i) {
                        lionSmallCount += lionInfo[i];
                        finalLionSmallCount += result[i];
                        if(lionSmallCount > finalLionSmallCount) {
                            result = lionInfo.clone();
                            break;
                        }
                    }
                }
            }
            return;
        }

        for(int j = 0; j <= 10; ++j) {
            ++lionInfo[j];
            dfs(limit, count + 1, apeachInfo, lionInfo);
            --lionInfo[j];
        }
    }

    public static int[] solution(int n, int[] info) {
        int[] lionInfo = new int[11];
        dfs(n, 0, info, lionInfo);
        return result;
    }

    public static void main(String[] args) {
        int n = 9;
        int[] info = {0,0,1,2,0,1,1,1,1,1,1};

        int[] yeah = solution(n, info);
        for(int data : yeah) {
            System.out.print(data + " ");
        }
    }
}