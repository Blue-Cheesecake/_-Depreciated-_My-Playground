package Basic;

import java.util.ArrayList;
import java.util.Collections;

public class Test_KthLargest {

    ArrayList<Integer> list = new ArrayList<Integer>();
    int k;
    // ! n log n + n

    // ! 2 3 4 5 8
    public Test_KthLargest(int k, int[] nums) {

        for (int i = 0; i < nums.length; i++) {
            list.add(nums[i]);
        }

        Collections.sort(list);
        this.k = k;

    }

    public int add(int val) {

        boolean added = false;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) >= val) {
                list.add(i, val);
                added = true;
                break;
            }
        }
        if (!added) {
            list.add(list.size(), val);
        }

        return list.get(list.size() - this.k);

    }
}
