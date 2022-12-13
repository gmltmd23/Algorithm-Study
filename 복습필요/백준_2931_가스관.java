import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

enum BlockType {
    EMPTY("."), COLUMN("|"), ROW("-"),
    PLUS("+"), ONE("1"), TWO("2"), THREE("3"), FOUR("4"),
    MOSCOV("M"), ZAGREV("Z");

    BlockType(String asString) {
        this.asString = asString;
    }
    private final String asString;

    public String toString() {
        return this.asString;
    }

    public boolean equals(String str) {
        return this.asString.equals(str);
    }
}

enum Direction {
    LEFT(0), RIGHT(1), UP(2), DOWN(3), DEFAULT(-1);

    public int getDirection() {
        return this.direction;
    }

    private Direction(final int direction) {
        this.direction = direction;
    }

    private final int direction;
}

class NowState {
    public NowState(int x, int y) {
        this.x = x;
        this.y = y;
        this.direction = Direction.DEFAULT;
    }

    public int x, y;
    public Direction direction;
}

class Block {
    public Block(BlockType blockType) {
        this.blockType = blockType;
    }

    public BlockType getBlockType() {
        return this.blockType;
    }

    public void judgeNextDirection(NowState nowState) {

    }

    public boolean canAccept(NowState nowState) {
        return true;
    }

    public char getBlockTypeChar() {
        if(blockType == BlockType.MOSCOV)
            return 'M';
        else
            return 'Z';
    }

    private BlockType blockType;
}

class EmptyBlock extends Block {
    public EmptyBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return false;
    }

    @Override
    public char getBlockTypeChar() {
        return '.';
    }
}

class ColumnBlock extends Block {
    public ColumnBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.LEFT) && (nowState.direction != Direction.RIGHT);
    }

    @Override
    public char getBlockTypeChar() {
        return '|';
    }
}

class RowBlock extends Block {
    public RowBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.UP) && (nowState.direction != Direction.DOWN);
    }

    @Override
    public char getBlockTypeChar() {
        return '-';
    }
}

class PlusBlock extends Block {
    public PlusBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return true;
    }

    @Override
    public char getBlockTypeChar() {
        return '+';
    }
}

class OneBlock extends Block {
    public OneBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public void judgeNextDirection(NowState nowState) {
        if(nowState.direction == Direction.UP)
            nowState.direction = Direction.RIGHT;
        else
            nowState.direction = Direction.DOWN;
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.RIGHT) && (nowState.direction != Direction.DOWN);
    }

    @Override
    public char getBlockTypeChar() {
        return '1';
    }
}

class TwoBlock extends Block {
    public TwoBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public void judgeNextDirection(NowState nowState) {
        if(nowState.direction == Direction.DOWN)
            nowState.direction = Direction.RIGHT;
        else
            nowState.direction = Direction.UP;
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.RIGHT) && (nowState.direction != Direction.UP);
    }

    @Override
    public char getBlockTypeChar() {
        return '2';
    }
}

class ThreeBlock extends Block {
    public ThreeBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public void judgeNextDirection(NowState nowState) {
        if(nowState.direction == Direction.RIGHT)
            nowState.direction = Direction.UP;
        else
            nowState.direction = Direction.LEFT;
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.UP) && (nowState.direction != Direction.LEFT);
    }

    @Override
    public char getBlockTypeChar() {
        return '3';
    }
}

class FourBlock extends Block {
    public FourBlock(BlockType blockType) {
        super(blockType);
    }

    @Override
    public void judgeNextDirection(NowState nowState) {
        if(nowState.direction == Direction.RIGHT)
            nowState.direction = Direction.DOWN;
        else
            nowState.direction = Direction.LEFT;
    }

    @Override
    public boolean canAccept(NowState nowState) {
        return (nowState.direction != Direction.DOWN) && (nowState.direction != Direction.RIGHT);
    }

    @Override
    public char getBlockTypeChar() {
        return '4';
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        graph = new Block[R][C];

        for(int i = 0; i < R; ++i) {
            String line = br.readLine();
            for(int j = 0; j < C; ++j) {
                graph[i][j] = buildBlock(line.charAt(j));
                if(graph[i][j].getBlockType() == BlockType.MOSCOV)
                    nowState = new NowState(i, j);
            }
        }

        for(int i = 0; i < 4; ++i) {
            int nextX = nowState.x + dx[i];
            int nextY = nowState.y + dy[i];
            if(isIncludeGraph(nextX, nextY)) {
                BlockType blockType = graph[nextX][nextY].getBlockType();
                if((blockType != BlockType.EMPTY) && (blockType != BlockType.ZAGREV)) {
                    nowState.x = nextX;
                    nowState.y = nextY;
                    nowState.direction = Direction.values()[i];
                    graph[nextX][nextY].judgeNextDirection(nowState);
                    break;
                }
            }
        }

        while(graph[nowState.x][nowState.y].getBlockType() != BlockType.EMPTY) {
            int nextX = nowState.x + dx[nowState.direction.getDirection()];
            int nextY = nowState.y + dy[nowState.direction.getDirection()];
            nowState.x = nextX;
            nowState.y = nextY;
            if(graph[nextX][nextY].getBlockType() != BlockType.EMPTY)
                graph[nextX][nextY].judgeNextDirection(nowState);
        }

        // 해커가 없애버린 블록에 도달했음
        answerX = nowState.x + 1;
        answerY = nowState.y + 1;

        // 없애버린 블록에서 방향모으기
        Direction reverseDirection = getReverseDirection(nowState.direction);
        LinkedList<Direction> directionList = new LinkedList<>();
        int beforeX = nowState.x + dx[reverseDirection.getDirection()];
        int beforeY = nowState.y + dy[reverseDirection.getDirection()];
        for(int i = 0; i < 4; ++i) {
            int nextX = nowState.x + dx[i];
            int nextY = nowState.y + dy[i];

            if(nextX != beforeX || nextY != beforeY) {
                if(isIncludeGraph(nextX, nextY)) {
                    Direction saveNowDirection = nowState.direction;
                    nowState.direction = getDirectionAsInteger(i);
                    if(graph[nextX][nextY].canAccept(nowState))
                        directionList.add(nowState.direction);
                    nowState.direction = saveNowDirection;
                }
            }
        }

        if(directionList.size() == 3)
            answerBlockType = '+';
        else
            answerBlockType = getAnswerBlockType(nowState.direction, directionList.getFirst());

        System.out.println(answerX + " " + answerY + " " + answerBlockType);

        br.close();
    }

    private static boolean isIncludeGraph(int x, int y) {
        if(0 <= x && x < R && 0 <= y && y < C)
            return true;
        return false;
    }

    private static char getAnswerBlockType(Direction originalDirection, Direction nextDirection) {
        Block[] blocks = new Block[6];
        blocks[0] = new ColumnBlock(BlockType.COLUMN);
        blocks[1] = new RowBlock(BlockType.ROW);
        blocks[2] = new OneBlock(BlockType.ONE);
        blocks[3] = new TwoBlock(BlockType.TWO);
        blocks[4] = new ThreeBlock(BlockType.THREE);
        blocks[5] = new FourBlock(BlockType.FOUR);

        for(int i = 0; i < 6; ++i) {
            NowState mockState = new NowState(0, 0);
            mockState.direction = originalDirection;

            if(blocks[i].canAccept(mockState)) {
                blocks[i].judgeNextDirection(mockState);
                if(mockState.direction == nextDirection)
                    return blocks[i].getBlockTypeChar();
            }
        }

        return 'X';
    }

    private static Direction getDirectionAsInteger(int direction) {
        Direction element = null;
        switch(direction) {
            case 0:
                element = Direction.LEFT;
                break;
            case 1:
                element = Direction.RIGHT;
                break;
            case 2:
                element = Direction.UP;
                break;
            case 3:
                element = Direction.DOWN;
                break;
            default:
                element = Direction.DEFAULT;
                break;
        }
        return element;
    }

    private static Direction getReverseDirection(Direction direction) {
        Direction reverseDirection = Direction.DEFAULT;
        switch(direction) {
            case RIGHT:
                reverseDirection = Direction.LEFT;
                break;
            case LEFT:
                reverseDirection = Direction.RIGHT;
                break;
            case UP:
                reverseDirection = Direction.DOWN;
                break;
            case DOWN:
                reverseDirection = Direction.UP;
                break;
        }
        return reverseDirection;
    }

    private static Block buildBlock(char blockString) {
        Block block = null;
        switch(blockString) {
            case '.':
                block = new EmptyBlock(BlockType.EMPTY);
                break;
            case '|':
                block = new ColumnBlock(BlockType.COLUMN);
                break;
            case '-':
                block = new RowBlock(BlockType.ROW);
                break;
            case '+':
                block = new PlusBlock(BlockType.PLUS);
                break;
            case '1':
                block = new OneBlock(BlockType.ONE);
                break;
            case '2':
                block = new TwoBlock(BlockType.TWO);
                break;
            case '3':
                block = new ThreeBlock(BlockType.THREE);
                break;
            case '4':
                block = new FourBlock(BlockType.FOUR);
                break;
            default:
                if(blockString == 'M')
                    block = new Block(BlockType.MOSCOV);
                else
                    block = new Block(BlockType.ZAGREV);
                break;
        }

        return block;
    }

    private static int R, C;
    private static NowState nowState = null;
    private static Block[][] graph;
    private static int answerX, answerY;
    private static char answerBlockType;

    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
}