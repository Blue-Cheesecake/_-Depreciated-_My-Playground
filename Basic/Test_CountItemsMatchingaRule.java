// https://leetcode.com/problems/count-items-matching-a-rule/

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        // ! items[i] = [type, color, name]
        int count = 0;

        for (List<String> list : items) {
            if (ruleKey.equals("type") && ruleValue.equals(list.get(0))) {
                count++;
            }
            if (ruleKey.equals("color") && ruleValue.equals(list.get(1))) {
                count++;
            }
            if (ruleKey.equals("name") && ruleValue.equals(list.get(2))) {
                count++;
            }
        }

        return count;
    }
}
