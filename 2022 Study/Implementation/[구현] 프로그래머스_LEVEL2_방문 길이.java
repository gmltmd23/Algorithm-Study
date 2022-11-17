import java.util.*;

class Main {
    static class WayLog {
        private int x, y;
        private int nx, ny;

        public WayLog(int x, int y, int nx, int ny) {
            this.x = x;
            this.y = y;
            this.nx = nx;
            this.ny = ny;
        }

        @Override
        public boolean equals(Object other) {
            if(this.getClass() != other.getClass())
                return false;

            WayLog castedOtherInstance = (WayLog)other;
            return (this.x == castedOtherInstance.x) && (this.y == castedOtherInstance.y) && (this.nx == castedOtherInstance.nx) && (this.ny == castedOtherInstance.ny);
        }

        @Override
        public int hashCode() {
            return (x + y + nx + ny);
        }
    }

    public static int solution(String dirs) {
        HashSet<WayLog> waySet = new HashSet<>();
        HashMap<Character, Integer> direction = new HashMap<>();
        char[] directionToCharArray = {'L', 'R', 'U', 'D'};
        for(int i = 0; i < 4; ++i)
            direction.put(directionToCharArray[i], i);

        int[] dx = {0, 0, 1, -1};
        int[] dy = {-1, 1, 0, 0};
        int x = 0;
        int y = 0;

        int answer = 0;
        for(int i = 0; i < dirs.length(); ++i) {
            int dir = direction.get(dirs.charAt(i));
            int nx = (x + dx[dir]);
            int ny = (y + dy[dir]);

            if(Math.abs(nx) <= 5 && Math.abs(ny) <= 5) {
                WayLog wayLog = new WayLog(x, y, nx, ny);
                WayLog reverseWayLog = new WayLog(nx, ny, x, y);
                if(!waySet.contains(wayLog) && !waySet.contains(reverseWayLog)) {
                    waySet.add(wayLog);
                    waySet.add(reverseWayLog);
                    answer += 1;
                }
                x = nx;
                y = ny;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        String dirs = "ULURRDLLU";
        System.out.println(solution(dirs));
    }
}