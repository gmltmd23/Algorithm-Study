import java.util.Arrays;

public class Main {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int indexOfA = 0;
        int indexOfB = 0;

        int answer = 0;
        while(indexOfA < A.length && indexOfB < B.length) {
            if(A[indexOfA] < B[indexOfB]) {
                ++answer;
                ++indexOfA;
            }
            ++indexOfB;
        }

        return answer;
    }
}