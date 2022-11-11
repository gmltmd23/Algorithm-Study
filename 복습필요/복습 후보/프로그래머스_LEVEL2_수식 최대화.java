import java.util.*;

public class Main {
    private static char[] previewOperators = {'*', '+', '-'};
    private static boolean[] visited = new boolean[3];
    private static ArrayList<Integer> originNumberList = new ArrayList<>();
    private static ArrayList<Character> originOperatorList = new ArrayList<>();
    private static int answer = 0;

    public static void makeOperatorOrder(ArrayList<Character[]> operatorOrderList, Character[] nowOperators, int step) {
        if(step == 3) {
            operatorOrderList.add(nowOperators.clone());
            return;
        }

        for(int i = 0; i < 3; ++i) {
            if(!visited[i]) {
                visited[i] = true;
                nowOperators[step] = previewOperators[i];
                makeOperatorOrder(operatorOrderList, nowOperators, step + 1);
                visited[i] = false;
            }
        }
    }

    public static void getAnswer(ArrayList<Character[]> operatorOrderList) {
        for(Character[] operatorOrder : operatorOrderList) {
            Deque<Integer> numberDeque = new ArrayDeque<>();
            Deque<Character> operatorDeque = new ArrayDeque<>();
            numberDeque.addAll(originNumberList);
            operatorDeque.addAll(originOperatorList);

            for(char nowOrder : operatorOrder) {
                int operatorDequeSize = operatorDeque.size();
                for(int i = 0; i < operatorDequeSize; ++i) {
                    int frontNumber = numberDeque.pollFirst();
                    char frontOperator = operatorDeque.pollFirst();

                    if(frontOperator == nowOrder) {
                        switch (frontOperator) {
                            case '*':
                                numberDeque.addFirst(frontNumber * numberDeque.pollFirst());
                                break;
                            case '+':
                                numberDeque.addFirst(frontNumber + numberDeque.pollFirst());
                                break;
                            case '-':
                                numberDeque.addFirst(frontNumber - numberDeque.pollFirst());
                                break;
                        }
                    }
                    else {
                        numberDeque.add(frontNumber);
                        operatorDeque.add(frontOperator);
                    }
                }
            }
            answer = Math.max(answer, Math.abs(numberDeque.getFirst()));
        }
    }

    public static long solution(String expression) {
        StringTokenizer st = new StringTokenizer(expression, "*-+");

        while(st.hasMoreTokens())
            originNumberList.add(Integer.parseInt(st.nextToken()));
        for(int i = 0; i < expression.length(); ++i) {
            char isOperator = expression.charAt(i);
            if(isOperator == '*' || isOperator == '-' || isOperator == '+')
                originOperatorList.add(isOperator);
        }

        ArrayList<Character[]> operatorOrderList = new ArrayList<>();
        makeOperatorOrder(operatorOrderList, new Character[3], 0);
        getAnswer(operatorOrderList);

        return answer;
    }

    public static void main(String[] args) {
        String expression = "100-200*300-500+20";
        System.out.println(solution(expression));
    }
}