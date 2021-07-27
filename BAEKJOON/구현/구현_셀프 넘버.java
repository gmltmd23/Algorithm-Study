/*
*
* 백준 문제 4673번 셀프 넘버
*
* 이것도 간단한 구현문제이다. 브루트포스 방식으로 1부터 찾으면 금방풀수있는 문제이다.
*
* */


class Main {
    public static void main(String[] args) {
        int n = 10001;
        boolean[] numbers = new boolean[n];
        for (int i = 1; i < n; i++) {
            int total = i;
            for (char c : Integer.toString(i).toCharArray())
                total += Integer.parseInt(String.valueOf(c));
            if (total < n && !numbers[total])
                numbers[total] = true;
        }

        for (int i = 1; i < n; i++) {
            if (!numbers[i])
                System.out.println(i);
        }
    }
}