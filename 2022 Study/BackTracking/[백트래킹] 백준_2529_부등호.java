import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        inEqualitySignArray = new char[K];
        visited = new boolean[10];
        satisfiedNumberList = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < K; ++i)
            inEqualitySignArray[i] = st.nextToken().charAt(0);

        for(int i = 0; i <= 9; ++i) {
            String nowString = Integer.toString(i);
            visited[i] = true;
            backTracking(0, nowString);
            visited[i] = false;
        }

        System.out.print(satisfiedNumberList.get(satisfiedNumberList.size() - 1) + "\n" + satisfiedNumberList.get(0));
    }

    public static void backTracking(int nowDepth, String nowString) {
        if(nowDepth == K) {
            satisfiedNumberList.add(nowString);
            return;
        }

        int lastNumber = Character.getNumericValue(nowString.charAt(nowString.length() - 1));
        for(int i = 0; i <= 9; ++i) {
            if(!visited[i])
            {
                if(isOkay(inEqualitySignArray[nowDepth], lastNumber, i)) {
                    visited[i] = true;
                    backTracking(nowDepth + 1, nowString + Integer.toString(i));
                    visited[i] = false;
                }
            }

        }
    }

    public static boolean isOkay(char inEqualitySign, int leftNumber, int rightNumber) {
        switch(inEqualitySign) {
            case '<':
                if(leftNumber < rightNumber)
                    return true;
                break;
            case '>':
                if(leftNumber > rightNumber)
                    return true;
                break;
            default:
                break;
        }

        return false;
    }

    private static int K;
    private static boolean[] visited;
    private static char[] inEqualitySignArray;
    private static ArrayList<String> satisfiedNumberList;
}