/*
*
* 백준 문제 10974번 그래프 탐색_모든 순열
*
* 자바에서는 permutations 라이브러리를 지원하지 않기때문에,
* 재귀함수를 통한 방법으로 구현해야만 한다.
* 따지고 보면 DFS 방법과 유사해서 분류를 그래프 탐색에 둔다.
*
* 구현하는 방법은 아래와 같이 visited를 이용하는 방법과
* 또 swap를 이용한 방법이 존재한다.
*
* 근데 visited를 이용한 방법은 순열이 예쁘게 오름차순으로 정렬되서 나오기때문에 이것을 사용했다.
* 복습하자.
*
* */

import java.util.*;

class Main {
    private static void permutation(int[] arr, int[] output, boolean[] visited, int depth, int limit) {
        if (depth == limit) {
            for (int i = 0; i < limit; i++) {
                System.out.print(output[i] + " ");
            }
            System.out.print("\n");
            return;
        }

        for (int i = 0; i < limit; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = arr[i];
                permutation(arr, output, visited, depth + 1, limit);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++)
            arr[i] = (i + 1);
        int[] output = new int[N];
        boolean[] visited = new boolean[N];

        permutation(arr, output, visited, 0, N);
    }
}