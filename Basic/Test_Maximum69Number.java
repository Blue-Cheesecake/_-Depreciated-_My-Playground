package Basic;

// https://leetcode.com/problems/maximum-69-number/

/**
 * Test_Maximum69Number
 */
public class Test_Maximum69Number {

    public int maximum69Number(int num) {

        String val = Integer.toString(num);
        val = val.replaceFirst("6", "9");
        int result = Integer.parseInt(val);
        return result;

    }

    public static void main(String[] args) {

        Test_Maximum69Number Solution = new Test_Maximum69Number();
        System.out.println(Solution.maximum69Number(9669));
    }
}