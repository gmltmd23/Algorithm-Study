import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        if(this.getClass() != obj.getClass())
            return false;
        return (this.x == ((Point)obj).x) && (this.y == ((Point)obj).y);
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    public int x, y;
}

class MoveWay {
    public MoveWay(int n, int m, int[][] graph, Point nowPosition) {
        fourDirectionList = new ArrayList<>();
        this.n = n;
        this.m = m;
        this.graph = graph;
        this.nowPosition = nowPosition;
    }

    public void makeCoverageSetList() {
        goAndInsertHashSet();
    }

    protected HashSet<Point> goUp() {
        HashSet<Point> coverageSet = new HashSet<>();
        for(int x = nowPosition.x; x >= 0; --x) {
            if(graph[x][nowPosition.y] == 0)
                coverageSet.add(new Point(x, nowPosition.y));
            if(graph[x][nowPosition.y] == 6)
                break;
        }
        return coverageSet;
    }

    protected HashSet<Point> goDown() {
        HashSet<Point> coverageSet = new HashSet<>();
        for(int x = nowPosition.x; x < n; ++x) {
            if(graph[x][nowPosition.y] == 0)
                coverageSet.add(new Point(x, nowPosition.y));
            if(graph[x][nowPosition.y] == 6)
                break;
        }
        return coverageSet;
    }

    protected HashSet<Point> goLeft() {
        HashSet<Point> coverageSet = new HashSet<>();
        for(int y = nowPosition.y; y >= 0; --y) {
            if(graph[nowPosition.x][y] == 0)
                coverageSet.add(new Point(nowPosition.x, y));
            if(graph[nowPosition.x][y] == 6)
                break;
        }
        return coverageSet;
    }

    protected HashSet<Point> goRight() {
        HashSet<Point> coverageSet = new HashSet<>();
        for(int y = nowPosition.y; y < m; ++y) {
            if(graph[nowPosition.x][y] == 0)
                coverageSet.add(new Point(nowPosition.x, y));
            if(graph[nowPosition.x][y] == 6)
                break;
        }
        return coverageSet;
    }

    protected void goAndInsertHashSet() {
        // URDL 순으로 저장
        fourDirectionList.add(goUp());
        fourDirectionList.add(goRight());
        fourDirectionList.add(goDown());
        fourDirectionList.add(goLeft());
    }

    public final static ArrayList<LinkedList<HashSet<Point>>> everyCoverageSetList = new ArrayList<>();
    protected ArrayList<HashSet<Point>> fourDirectionList;
    private int n, m;
    private int[][] graph;
    private Point nowPosition;
}

class FirstWay extends MoveWay {
    public FirstWay(int n, int m, int[][] graph, Point nowPosition) {
        super(n, m, graph, nowPosition);
    }

    @Override
    public void makeCoverageSetList() {
        super.makeCoverageSetList();

        LinkedList<HashSet<Point>> temp = new LinkedList<>();
        temp.addAll(fourDirectionList);

        everyCoverageSetList.add(temp);
    }
}

class SecondWay extends MoveWay {
    public SecondWay(int n, int m, int[][] graph, Point nowPosition) {
        super(n, m, graph, nowPosition);
    }

    @Override
    public void makeCoverageSetList() {
        super.makeCoverageSetList();

        LinkedList<HashSet<Point>> temp = new LinkedList<>();
        for(int i = 0; i < 2; ++i) {
            HashSet<Point> tempSet = new HashSet<>(fourDirectionList.get(i));
            tempSet.addAll(fourDirectionList.get(i + 2));
            temp.add(tempSet);
        }

        everyCoverageSetList.add(temp);
    }
}

class ThirdWay extends MoveWay {
    public ThirdWay(int n, int m, int[][] graph, Point nowPosition) {
        super(n, m, graph, nowPosition);
    }

    @Override
    public void makeCoverageSetList() {
        super.makeCoverageSetList();

        LinkedList<HashSet<Point>> temp = new LinkedList<>();
        for(int i = 0; i < 4; ++i) {
            int first = i;
            int second = (i + 1) % 4;
            HashSet<Point> tempSet = new HashSet<>(fourDirectionList.get(first));
            tempSet.addAll(fourDirectionList.get(second));
            temp.add(tempSet);
        }

        everyCoverageSetList.add(temp);
    }
}

class FourthWay extends MoveWay {
    public FourthWay(int n, int m, int[][] graph, Point nowPosition) {
        super(n, m, graph, nowPosition);
    }

    @Override
    public void makeCoverageSetList() {
        super.makeCoverageSetList();

        LinkedList<HashSet<Point>> temp = new LinkedList<>();
        for(int i = 0; i < 4; ++i) {
            int first = i;
            int second = (i - 1) % 4;
            if(second < 0)
                second += 4;
            int third = (i + 1) % 4;
            HashSet<Point> tempSet = new HashSet<>(fourDirectionList.get(first));
            tempSet.addAll(fourDirectionList.get(second));
            tempSet.addAll(fourDirectionList.get(third));
            temp.add(tempSet);
        }

        everyCoverageSetList.add(temp);
    }
}

class FifthWay extends MoveWay {
    public FifthWay(int n, int m, int[][] graph, Point nowPosition) {
        super(n, m, graph, nowPosition);
    }

    @Override
    public void makeCoverageSetList() {
        super.makeCoverageSetList();

        LinkedList<HashSet<Point>> temp = new LinkedList<>();
        HashSet<Point> tempSet = new HashSet<>(fourDirectionList.get(0));
        tempSet.addAll(fourDirectionList.get(1));
        tempSet.addAll(fourDirectionList.get(2));
        tempSet.addAll(fourDirectionList.get(3));
        temp.add(tempSet);

        everyCoverageSetList.add(temp);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        cctvList = new ArrayList<>();

        blindSpot = 0;
        for(int i = 0; i < n; ++i) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < m; ++j) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if(graph[i][j] == 0) {
                    ++blindSpot;
                }
                else {
                    if(graph[i][j] != 6)
                        cctvList.add(new Point(i, j));
                }
            }
        }

        for(Point point : cctvList) {
            MoveWay moveWay = makeMoveWay(point);
            moveWay.makeCoverageSetList();
        }

        result = Integer.MAX_VALUE;
        process(MoveWay.everyCoverageSetList.size(), 0, new HashSet<>());

        System.out.println(result);
    }

    private static MoveWay makeMoveWay(Point point) {
        MoveWay moveWay = null;
        switch(graph[point.x][point.y]) {
            case 1:
                moveWay = new FirstWay(n, m, graph, point);
                break;
            case 2:
                moveWay = new SecondWay(n, m, graph, point);
                break;
            case 3:
                moveWay = new ThirdWay(n, m, graph, point);
                break;
            case 4:
                moveWay = new FourthWay(n, m, graph, point);
                break;
            case 5:
                moveWay = new FifthWay(n, m, graph, point);
                break;
            default:
                break;
        }

        return moveWay;
    }

    private static void process(final int maxDepth, int nowDepth, HashSet<Point> beforeHashSet) {
        if(nowDepth < maxDepth) {
            LinkedList<HashSet<Point>> coverageList = MoveWay.everyCoverageSetList.get(nowDepth);
            for(HashSet<Point> element : coverageList) {
                HashSet<Point> nextHashSet = new HashSet<>(beforeHashSet);
                nextHashSet.addAll(element);

                if(nowDepth == maxDepth - 1)
                    result = Math.min(result, (blindSpot - nextHashSet.size()));
                else
                    process(maxDepth, nowDepth + 1, nextHashSet);
            }
        }
    }

    private static int result;
    private static int n, m, blindSpot;
    private static ArrayList<Point> cctvList;
    private static int[][] graph;
}