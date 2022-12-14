public class Main {
    public static int solution(int n, int a, int b) {
        int answer = 0;
        while(a != b) {
            if(a != 1)
                a = (a / 2) + (a % 2);
            if(b != 1)
                b = (b / 2) + (b % 2);
            ++answer;
        }

        return answer;
    }

    public static void main(String[] args) {
        int n = 8;
        int a = 4;
        int b = 7;
        System.out.println(solution(n, a, b));
    }
}