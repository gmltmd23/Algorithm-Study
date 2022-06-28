/*
*
* 백준 문제 1157번 단어 공부
*
* 일명 딕셔너리(해쉬맵)을 쓰면 금방 풀수있는 문제긴한데
* 코드좀 이쁘게 만들려고 하니 Pair 클래스를 만들어야되서 의도치않게 코드가 길어졌다.
*
* 자바는 저저저 세터 게터좀 코틀린처럼 자동으로 생성되면 좋겠다..
*
* */

import java.util.HashMap;
import java.util.Scanner;

class Pair {
    private int x;
    private int y;
    private char c1;
    private char c2;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
        this.c1 = 'K';
        this.c2 = 'K';
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return y;
    }

    public void setC1(char c1) {
        this.c1 = c1;
    }

    public char getC1() {
        return c1;
    }

    public void setC2(char c2) {
        this.c2 = c2;
    }

    public char getC2() {
        return c2;
    }
}

class Main {
    private static String everything = "abcdefghijklmnopqrstuvwxyz";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Character, Integer> alphabet = makeHashMap();
        String data = sc.nextLine().trim().toLowerCase();
        for (char c : data.toCharArray())
            alphabet.put(c, alphabet.get(c) + 1);

        Pair result = getMaximum(alphabet);
        if (result.getX() == result.getY())
            System.out.println("?");
        else
            System.out.println(Character.toUpperCase(result.getC1()));
    }

    private static HashMap<Character, Integer> makeHashMap() {
        HashMap<Character, Integer> temp = new HashMap<>();
        for (char alphabet : everything.toCharArray())
            temp.put(alphabet, 0);
        return temp;
    }

    private static Pair getMaximum(HashMap<Character, Integer> alphabet) {
        Pair temp = new Pair(0, 0);
        for (char c : everything.toCharArray()) {
            int value = alphabet.get(c);
            if (value >= temp.getX()) {
                temp.setY(temp.getX());
                temp.setC2(temp.getC1());
                temp.setX(value);
                temp.setC1(c);
            }
        }
        return temp;
    }
}