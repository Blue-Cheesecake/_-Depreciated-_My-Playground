// https://leetcode.com/problems/number-of-segments-in-a-string/

public class Test_NumberOfSegmentsOfString {
    public int countSegments(String s) {

        if (s.equals("")) {
            return 0;
        }

        boolean found = false;
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
                found = true;
            }
            if (found) {
                if (s.charAt(i) == ' ') {
                    found = false;
                    result++;
                }
            }
        }

        if (found) {
            result++;
        }

        return result;

    }
}