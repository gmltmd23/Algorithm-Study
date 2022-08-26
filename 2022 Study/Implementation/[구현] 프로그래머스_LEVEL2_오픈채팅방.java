import java.util.*;

public class Main {
    public static String[] solution(String[] record) {
        HashMap<String, String> lastName = new HashMap<>();
        HashSet<String> room = new HashSet<>();
        ArrayList<String> userIdList = new ArrayList<>();

        for(String element : record)
            preprocess(element, lastName, userIdList);

        String[] answer = new String[userIdList.size()];
        for(int i = 0; i < answer.length; ++i) {
            String userID = userIdList.get(i);
            if(!room.contains(userID)) {
                room.add(userID);
                answer[i] = lastName.get(userID) + "님이 들어왔습니다.";
            }
            else {
                room.remove(userID);
                answer[i] = lastName.get(userID) + "님이 나갔습니다.";
            }
        }

        return answer;
    }

    private static void preprocess(String target, HashMap<String, String> lastName, ArrayList<String> resultList) {
        StringTokenizer st = new StringTokenizer(target, " ");
        String type = st.nextToken();
        String userID = st.nextToken();
        String userNickName = null;

        switch(type) {
            case "Enter":
                userNickName = st.nextToken();
                lastName.put(userID, userNickName);
            case "Leave":
                resultList.add(userID);
                break;
            case "Change":
                userNickName = st.nextToken();
                lastName.put(userID, userNickName);
                break;
        }
    }

    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        System.out.println(solution(record));
    }
}