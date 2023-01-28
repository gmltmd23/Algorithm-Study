public class Main {
    private static int answer;

    public static void dfs(final int target, int step, int total, int[] numbers) {
        if(step == numbers.length) {
            if(total == target)
                ++answer;
            return;
        }

        dfs(target, step + 1, total + numbers[step], numbers);
        dfs(target, step + 1, total - numbers[step], numbers);
    }

    public static int solution(int[] numbers, int target) {
        answer = 0;
        dfs(target, 0, 0, numbers);
        return answer;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(solution(numbers, target));
    }
}