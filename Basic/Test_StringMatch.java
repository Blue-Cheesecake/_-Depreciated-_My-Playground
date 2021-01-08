package Basic;

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<String> stringMatching(String[] words) {

        List<String> resultObject = new ArrayList<String>();

        int n = words.length;

        for (int i = 0; i < n; i++) {

            String prota = words[i];

            for (int j = 0; j < n; j++) {

                String nFind = words[j];

                if (!prota.equals(nFind) && prota.contains(nFind) && !resultObject.contains(nFind)) {
                    resultObject.add(nFind);

                }

            }
        }

        return resultObject;
    }

    public static void main(String[] args) {

        Solution result = new Solution();
        String[] add = { "blue", "green", "bu" };
        System.out.println(result.stringMatching(add));
    }
}
