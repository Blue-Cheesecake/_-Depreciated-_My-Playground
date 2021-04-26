// https://leetcode.com/problems/print-words-vertically/

import java.util.ArrayList;
import java.util.List;

public class Test_printWordVertically {

    public List<String> printVertically(String s) {

        List<String> result = new ArrayList<String>();
        List<String> arr = new ArrayList<String>();
        List<Integer> indexLastWord = new ArrayList<Integer>();
        String full = "";
        int max = 0;

        // find the max legnth of word and split string
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                arr.add(full);
                if (max <= full.length()) {
                    max = full.length();
                }
                full = "";
            } else {
                full += s.charAt(i);
            }
        }
        if (s.charAt(s.length() - 1) != ' ') {
            arr.add(full);
            if (max <= full.length()) {
                max = full.length();
            }
        }

        // add to result
        for (int i = 0; i < max; i++) {
            result.add("");
            indexLastWord.add(0);
            for (int j = 0; j < arr.size(); j++) {
                String str = arr.get(j);
                // base case
                if (i >= str.length()) {
                    result.set(i, result.get(i) + " ");
                    continue;
                }
                result.set(i, result.get(i) + str.charAt(i));
                indexLastWord.set(i, result.get(i).length());

            }
        }

        // remove Trailing spaces
        for (int i = 0; i < result.size(); i++) {
            result.set(i, result.get(i).substring(0, indexLastWord.get(i)));
        }

        return result;
    }

}

/**
 * Gel
 */
class Test_printWordVertically_Tester {
    public static void main(String[] args) {
        Test_printWordVertically sol = new Test_printWordVertically();
        System.out.println(sol.printVertically("HOW ARE YOU"));
        // [HAY, ORO, WEU]
        System.out.println(sol.printVertically("TO BE OR NOT TO BE"));
        // [TBONTB, OEROOE, ___T]
        System.out.println(sol.printVertically("CONTEST IS COMING"));
        // [CIC, OSO, N_M, T_I, E_N, S_G, T]
        System.out.println(sol.printVertically("HOW IS IT GOING"));
        // [HIIG, OSTO, W__I, ___N, ___G]
    }
}