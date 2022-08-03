import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

class Position {
    Position(int x, int y) {
        this._x = x;
        this._y = y;
    }

    public int getX() {
        return _x;
    }

    public int getY() {
        return _y;
    }

    private int _x;
    private int _y;
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        answer = Integer.MAX_VALUE;
        houseList = new ArrayList<>();
        chickenList = new ArrayList<>();
        stack = new Stack<>();

        for(int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int eachHouseIndex = 0; eachHouseIndex < N; ++eachHouseIndex) {
                int nowValue = Integer.parseInt(st.nextToken());
                if(nowValue == 1)
                    houseList.add(new Position(i, eachHouseIndex));
                else if(nowValue == 2)
                    chickenList.add(new Position(i, eachHouseIndex));
            }
        }

        dfs(M, 0, 0);
        System.out.println(answer);
        br.close();
    }

    public static void dfs(final int maximum, final int count, final int startIndex) {
        if(count == maximum) {
            realProcess();
            return;
        }

        for(int i = startIndex; i < chickenList.size(); ++i) {
            stack.push(chickenList.get(i));
            dfs(maximum, count + 1, startIndex + 1);
            stack.pop();
        }
    }

    public static void realProcess() {
        int result = 0;
        for(Position house : houseList) {
            int tempMinimumValue = Integer.MAX_VALUE;
            for(Position chickenHouse : stack) {
                int distance = Math.abs(chickenHouse.getX() - house.getX()) + Math.abs(chickenHouse.getY() - house.getY());
                tempMinimumValue = Math.min(tempMinimumValue, distance);
            }
            result += tempMinimumValue;
        }

        answer = Math.min(answer, result);
    }

    private static Stack<Position> stack;
    private static int answer;
    private static ArrayList<Position> houseList;
    private static ArrayList<Position> chickenList;
}