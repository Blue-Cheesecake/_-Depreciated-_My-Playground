// https://leetcode.com/problems/add-strings/

public class Test_AddStrings {

    public static int turnToInt(Character c) {
        return Character.getNumericValue(c);
    }

    public static String turnToString(int i) {
        return String.valueOf(i);
    }

    public String addStrings(String num1, String num2) {

        String result = "";
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        boolean exceed = false;

        while (i >= 0 || j >= 0) {

            int digit1 = 0;
            int digit2 = 0;

            if (i >= 0) {
                digit1 = turnToInt(num1.charAt(i));
            }
            if (j >= 0) {
                digit2 = turnToInt(num2.charAt(j));
            }

            int sum = digit1 + digit2;

            if (exceed) {
                sum++;
                exceed = false;
            }
            if (sum >= 10) {
                sum = sum % 10;
                exceed = true;
            }

            result = turnToString(sum) + result;

            i--;
            j--;
        }

        if (exceed) {
            result = "1" + result;
        }

        return result;
    }

}