import java.util.ArrayList;
import java.util.Collections;

class SortFile implements Comparable<SortFile> {
    public SortFile(String head, int number, String fileName) {
        this._head = head.toLowerCase();
        this._number = number;
        this._fileName = fileName;
    }

    public String   _head;
    public int      _number;
    public String   _fileName;

    @Override
    public int compareTo(SortFile other) {
        if(this._head.compareTo(other._head) == 0)
            return this._number - other._number;
        else
            return this._head.compareTo(other._head);
    }
}

public class Main {
    public static String[] solution(String[] files) {
        ArrayList<SortFile> fileList = new ArrayList<>();
        for(String fileName : files) {
            StringBuilder headBuilder = new StringBuilder();
            int numberIndex = 0;
            while(numberIndex < fileName.length() && !Character.isDigit(fileName.charAt(numberIndex)))
                headBuilder.append(fileName.charAt(numberIndex++));

            StringBuilder numberBuilder = new StringBuilder();
            while(numberIndex < fileName.length() && Character.isDigit(fileName.charAt(numberIndex)))
                numberBuilder.append(fileName.charAt(numberIndex++));

            fileList.add(new SortFile(headBuilder.toString(), Integer.parseInt(numberBuilder.toString()), fileName));
        }

        Collections.sort(fileList);
        String[] answer = new String[fileList.size()];
        for(int i = 0; i < fileList.size(); ++i)
            answer[i] = fileList.get(i)._fileName;

        return answer;
    }

    public static void main(String[] args) {
        String[] files = {"MUZI01.zip", "muzi1.png"};
        String[] result = solution(files);

        for(String element : result)
            System.out.print(element + " ");
    }
}