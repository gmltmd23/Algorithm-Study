import java.util.*;

public class Main {
    public static String[] solution(String[][] tickets) {
        Map<String, Stack<String>> ticketMap = new HashMap<>();
        for(String[] eachTicket : tickets) {
            if(!ticketMap.containsKey(eachTicket[0]))
                ticketMap.put(eachTicket[0], new Stack<>());
            ticketMap.get(eachTicket[0]).push(eachTicket[1]);
        }
        for(String key : ticketMap.keySet())
            Collections.sort(ticketMap.get(key), Collections.reverseOrder());

        Stack<String> stack = new Stack<>();
        stack.push("ICN");

        Stack<String> answerStack = new Stack<>();
        while(!stack.isEmpty()) {
            String location = stack.peek();
            if(ticketMap.containsKey(location) && !ticketMap.get(location).isEmpty())
                stack.push(ticketMap.get(location).pop());
            else
                answerStack.push(stack.pop());
        }

        String[] answer = new String[answerStack.size()];
        for(int i = 0; i < answer.length; ++i)
            answer[i] = answerStack.pop();

        return answer;
    }

    public static void main(String[] args) {
        String[][] tickets = {{"ICN", "A"}, {"ICN", "B"}, {"A", "D"}, {"B", "C"}};
        System.out.println(solution(tickets));
    }
}