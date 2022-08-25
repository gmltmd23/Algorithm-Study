import java.util.HashMap;

public class Main {
    public static String solution(String[] survey, int[] choices) {
        String[] indicators = {"RT", "CF", "JM", "AN"};
        HashMap<Character, Integer> scoreTable = new HashMap<>();

        for(String element : indicators) {
            char left = element.charAt(0);
            char right = element.charAt(1);
            scoreTable.put(left, 0);
            scoreTable.put(right, 0);
        }

        for(int i = 0; i < survey.length; ++i)
            processScore(scoreTable, survey[i], choices[i]);

        StringBuilder answer = new StringBuilder();
        for(String target : indicators) {
            int leftScore = scoreTable.get(target.charAt(0));
            int rightScore = scoreTable.get(target.charAt(1));

            if(leftScore > rightScore)
                answer.append(target.charAt(0));
            else if(leftScore < rightScore)
                answer.append(target.charAt(1));
            else
                answer.append(getCharacterAsOrder(target.charAt(0), target.charAt(1)));
        }

        return answer.toString();
    }

    private static char getCharacterAsOrder(char left, char right) {
        if(left < right)
            return left;
        else
            return right;
    }

    private static void processScore(HashMap<Character, Integer> scoreTable, String target, int choice) {
        int scale = 4 - choice;
        if(scale > 0) {
            char leftTarget = target.charAt(0);
            scoreTable.put(leftTarget, scoreTable.get(leftTarget) + scale);
        }
        else if(scale < 0) {
            char rightTarget = target.charAt(1);
            scoreTable.put(rightTarget, scoreTable.get(rightTarget) + Math.abs(scale));
        }
    }

    public static void main(String[] args) {
        String[] survey = {"TR", "RT", "TR"};
        int[] choices = {7, 1, 3};
        System.out.println(solution(survey, choices));
    }
}