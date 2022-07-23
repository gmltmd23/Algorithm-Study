class Solution {
    public void dfs(int[] numbers, int target, int total, int index, int[] answer) {
        if(index < (numbers.length - 1))
        {
            dfs(numbers, target, total + numbers[index + 1], index + 1, answer);
            dfs(numbers, target, total - numbers[index + 1], index + 1, answer);
        }
        else
        {
            if(total == target)
                ++answer[0];
        }
    }

    public int solution(int[] numbers, int target) {
        int[] answer = {0};

        dfs(numbers, target, numbers[0], 0, answer);
        dfs(numbers, target, -numbers[0], 0, answer);

        return answer[0];
    }
}