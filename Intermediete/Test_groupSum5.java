// https://codingbat.com/prob/p138907

package Intermediete;

public class Test_groupSum5 {

    public boolean groupSum5(int start, int[] nums, int target) {

        if (start >= nums.length) {
            return target == 0;
        }

        if (nums[start] % 5 == 0) {
            return groupSum5(start + 1, nums, target - nums[start]);
        }

        if (nums[start] == 1) {
            if (start != 0) {
                if (nums[start - 1] % 5 == 0) {
                    return groupSum5(start + 1, nums, target);
                }
            }
        }

        if (groupSum5(start + 1, nums, target - nums[start])) {
            return true;
        }

        return groupSum5(start + 1, nums, target);
    }
}
