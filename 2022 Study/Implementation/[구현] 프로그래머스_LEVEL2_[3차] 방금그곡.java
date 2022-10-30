import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static class Result implements Comparable<Result> {
        public int playTime;
        public int order;
        public String title;

        public Result(int playTime, int order, String title) {
            this.playTime = playTime;
            this.order = order;
            this.title = title;
        }

        @Override
        public int compareTo(Result other) {
            int playTimeDifference = this.playTime - other.playTime;
            if(playTimeDifference == 0)
                return this.order - other.order;
            else
                return -playTimeDifference;
        }
    }

    private static int calculatePlayTime(String startTime, String endTime) {
        String[] splitedStartTime = startTime.split(":");
        String[] splitedEndTime = endTime.split(":");

        int playTime = (Integer.parseInt(splitedEndTime[0]) - Integer.parseInt(splitedStartTime[0])) * 60;
        int startMinute = Integer.parseInt(splitedStartTime[1]);
        int endMinute = Integer.parseInt(splitedEndTime[1]);

        if(startMinute > endMinute)
            playTime -= (startMinute - endMinute);
        else
            playTime += (endMinute - startMinute);

        return playTime;
    }

    private static boolean isRightMusic(int playTime, String melody, String music) {
        StringBuilder stringBuilder = new StringBuilder();
        int musicLength = music.length();
        int index = 0;
        while(playTime > 0) {
            if((index + 1) < musicLength && music.charAt(index + 1) == '#')
                stringBuilder.append(music.charAt(index++));
            stringBuilder.append(music.charAt(index));
            index = (index + 1) % music.length();
            --playTime;
        }

        int foundIndex = stringBuilder.indexOf(melody);
        if(foundIndex == -1) {
            return false;
        }
        else {
            while(foundIndex != -1) {
                int maybeSharpIndex = foundIndex + melody.length();
                if(maybeSharpIndex < stringBuilder.length() && stringBuilder.charAt(maybeSharpIndex) != '#')
                    return true;
                if(maybeSharpIndex >= stringBuilder.length())
                    return true;
                stringBuilder.replace(foundIndex, maybeSharpIndex, "");
                foundIndex = stringBuilder.indexOf(melody);
            }

            return false;
        }
    }

    private static String solution(String m, String[] musicinfos) {
        ArrayList<Result> resultList = new ArrayList<>();
        for(int i = 0; i < musicinfos.length; ++i) {
            String[] splitedInfo = musicinfos[i].split(",");
            int playTime = calculatePlayTime(splitedInfo[0], splitedInfo[1]);
            String title = splitedInfo[2];
            if(isRightMusic(playTime, m, splitedInfo[3]))
                resultList.add(new Result(playTime, i, title));
        }
        Collections.sort(resultList);

        return (resultList.isEmpty()) ? "(None)" : resultList.get(0).title;
    }

    public static void main(String[] args) {
        String m = "CC#BCC#BCC#";
        String[] musicInfos = {"03:00,03:08,FOO,CC#B"};
        System.out.println(solution(m, musicInfos));
    }
}