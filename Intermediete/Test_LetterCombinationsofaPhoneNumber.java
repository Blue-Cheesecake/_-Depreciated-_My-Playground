// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution {
    public List<String> letterCombinations(String digits) {

        List<String> result = new ArrayList<String>();

        if (digits.length() == 0) {
            return result;
        }

        HashMap<Integer, String> dict = new HashMap<Integer, String>();
        dict.put(2, "abc");
        dict.put(3, "def");
        dict.put(4, "ghi");
        dict.put(5, "jkl");
        dict.put(6, "mno");
        dict.put(7, "pqrs");
        dict.put(8, "tuv");
        dict.put(9, "wxyz");

        int totalSize = dict.get(Integer.parseInt(digits.substring(0, 0 + 1))).length();
        for (int i = 1; i < digits.length(); i++) {
            totalSize *= dict.get(Integer.parseInt(digits.substring(i, i + 1))).length();
        }

        for (int i = 0; i < digits.length(); i++) {

            int eachDigit = Integer.parseInt(digits.substring(i, i + 1));
            String val = dict.get(eachDigit);
            int count = 1;
            if (i + 1 < digits.length()) {
                for (int j = i + 1; j < digits.length(); j++) {
                    count *= dict.get(Integer.parseInt(digits.substring(j, j + 1))).length();
                }
            }

            int indexResult = 0;
            while (indexResult < totalSize) {
                for (int j = 0; j < val.length(); j++) {
                    String eachChar = val.substring(j, j + 1);
                    for (int k = 0; k < count; k++) {
                        if (i == 0) {
                            result.add(eachChar);
                        } else {
                            result.set(indexResult, result.get(indexResult) + eachChar);
                        }
                        indexResult++;
                    }
                }
            }

        }

        return result;
    }
}
