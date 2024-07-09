public class Workshop {
    public static void main(String[] args) {
        doSomething("lolll", 5);
    }

    private static void doSomething(String action, int repeat) {
        for(int i = 1 ; i <= repeat ; i++) {
            System.out.println(action);
        }
    }
}