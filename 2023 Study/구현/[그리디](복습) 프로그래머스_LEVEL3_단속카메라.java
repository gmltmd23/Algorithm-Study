import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static int solution(int[][] routes) {
        Arrays.sort(routes, Comparator.comparingInt(left -> left[0]));

        int answer = 1;
        int limit = routes[0][1];
        for(int i = 0; i < routes.length; ++i) {
            int[] eachRoute = routes[i];
            if(limit < eachRoute[0]) {
                limit = eachRoute[1];
                ++answer;
            }
            else if(eachRoute[1] < limit) {
                limit = eachRoute[1];
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[][] routes = {{-20, -15}, {-14, -5}, {-18, -13}, {-5, -3}};
        //int[][] routes = {{-20, -2}, {-14, -10}, {-11, -8}, {-5, -3}};
        System.out.println(solution(routes));
    }
}