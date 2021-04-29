// https://leetcode.com/problems/truncate-sentence/

class Solution {
    public String truncateSentence(String s, int k) {
        String result = "";

        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                count++;
                if (count == k) {
                    break;
                }
            }
            result += s.charAt(i);
        }

        return result;
    }
}
