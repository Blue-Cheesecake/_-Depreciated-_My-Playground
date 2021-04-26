// https://leetcode.com/problems/custom-sort-string/

public class Test_CustomSortString {

    public String customSortString(String S, String T) {

        String result = "";

        for (int i = 0; i < S.length(); i++) {

            Character order = S.charAt(i);
            int j = 0;

            while (j < T.length()) {
                if (T.charAt(j) == order) {
                    result += order;
                    T = T.substring(0, j) + T.substring(j + 1);
                } else {
                    j++;
                }
            }

        }

        result += T;

        return result;
    }

}
