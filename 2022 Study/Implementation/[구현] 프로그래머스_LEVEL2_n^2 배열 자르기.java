public class Main {
    public static void main(String[] args) {
        int n = 3;
        int[] result = new int[(5 - 2) + 1];
        long left = 2;
        long right = 5;

        for(long i = left; i <= right; ++i) {
            int x = (int)(i / n);
            int y = (int)(i % n);
            result[(int)(i - left)] = Math.max(x, y) + 1;
        }

        for(int data : result) {
            System.out.println(data);
        }
    }
}