import java.util.*;

public class Main {
    public static String[] solution(String[] record) {
        Set<String> checkInSet = new HashSet<>();
        Map<String, String> nameMap = new HashMap<>();
        List<String> orderList = new ArrayList<>();
        for(String eachRecord : record) {
            StringTokenizer st = new StringTokenizer(eachRecord);
            String command = st.nextToken();
            if(command.equals("Change")) {
                String uid = st.nextToken();
                String name = st.nextToken();
                nameMap.put(uid, name);
            }
            else {
                orderList.add(st.nextToken());
                if(command.equals("Enter"))
                    nameMap.put(orderList.get(orderList.size() - 1), st.nextToken());
            }
        }

        StringBuilder sb = new StringBuilder();
        String[] result = new String[orderList.size()];
        for(int i = 0; i < orderList.size(); ++i) {
            String uid = orderList.get(i);
            if(!checkInSet.contains(uid)) {
                checkInSet.add(uid);
                result[i] = nameMap.get(uid) + "님이 들어왔습니다.";
            }
            else {
                result[i] = nameMap.get(uid) + "님이 나갔습니다.";
                checkInSet.remove(uid);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        String[] result = solution(record);
        for(String element : result) {
            System.out.println(element);
        }
        //System.out.println(solution(record));
    }
}