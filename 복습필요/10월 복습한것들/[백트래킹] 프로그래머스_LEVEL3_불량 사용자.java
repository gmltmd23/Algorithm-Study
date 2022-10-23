import java.util.ArrayList;
import java.util.HashSet;
import java.util.regex.Pattern;

public class Main {
    private static HashSet<HashSet<String>> answer;
    private static ArrayList<ArrayList<String>> bannedUserList;

    private static ArrayList<String> matchBannedId(String bannedId, String[] user_id) {
        String pattern = bannedId.replace('*', '.');
        ArrayList<String> valueList = new ArrayList<>();

        for(String userID : user_id) {
            boolean isMatch = Pattern.matches(pattern, userID);
            if(isMatch)
                valueList.add(userID);
        }

        return valueList;
    }

    private static void backTracking(HashSet<String> temp, final int nowDepth) {
        if(nowDepth == bannedUserList.size()) {
            answer.add(temp);
            return;
        }

        for(String userID : bannedUserList.get(nowDepth)) {
            if(!temp.contains(userID)) {
                temp.add(userID);
                backTracking(temp, nowDepth + 1);
                temp.remove(userID);
            }
        }
    }

    private static int solution(String[] user_id, String[] banned_id) {
        answer = new HashSet<>();
        bannedUserList = new ArrayList<>();
        for(String bannedID : banned_id)
            bannedUserList.add(matchBannedId(bannedID, user_id));
        backTracking(new HashSet<>(), 0);

        return answer.size();
    }

    public static void main(String[] args) {
        String[] user_id = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
        String[] banned_id = {"fr*d*", "abc1**"};
        System.out.println(solution(user_id, banned_id));
    }
}