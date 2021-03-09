import java.util.ArrayList;
import java.util.List;

/**
 * Test_DesignAnOrderedStream
 */
public class Test_DesignAnOrderedStream {

    public String[] arr;
    int ptr = 0;

    public Test_DesignAnOrderedStream(int n) {
        arr = new String[n];
    }

    public List<String> insert(int id, String value) {

        List<String> result = new ArrayList<String>();
        arr[id - 1] = value;
        int end = 0;
        int i;
        for (i = ptr; i < arr.length; i++) {
            if (arr[i] == null) {
                end = i;
                break;
            }
        }

        if (i == arr.length) {
            end = i;
        }

        for (i = ptr; i < end; i++) {
            result.add(arr[i]);
        }

        if (!result.isEmpty()) {
            ptr = end;
        }

        return result;
    }

    public static void main(String[] args) {
        Test_DesignAnOrderedStream os = new Test_DesignAnOrderedStream(5);
        System.out.println(os.insert(3, "ccccc")); // Inserts (3, "ccccc"), returns [].
        System.out.println(os.insert(1, "aaaaa")); // Inserts (1, "aaaaa"), returns ["aaaaa"].
        System.out.println(os.insert(2, "bbbbb")); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
        System.out.println(os.insert(5, "eeeee")); // Inserts (5, "eeeee"), returns [].
        System.out.println(os.insert(4, "ddddd")); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
        // Concatentating all the chunks returned:
        // [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa",
        // "bbbbb", "ccccc", "ddddd", "eeeee"]
        // The resulting order is the same as the order above.
    }
}
