// https://codingbat.com/prob/p105136

package Intermediete;

public class Test_GroupSumClump {

    public boolean groupSumClump(int start, int[] nums, int target) {

        if (start >= nums.length) {
            return target == 0;
        }

        // ! the identical value, they must either all be chosen, or none of them chosen
        // ! one loop can be used to find the extent of the identical values

        boolean iden = false;
        int to = start;

        for (int i = start + 1; i < nums.length; i++) {
            if (nums[i] == nums[start]) {
                to = i;
                iden = true;
            } else {
                break;
            }
        }

        if (iden) {
            return groupSumClump(to + 1, nums, target - (nums[start] * (to - start + 1)))
                    || groupSumClump(to + 1, nums, target);
        }

        if (groupSumClump(start + 1, nums, target - nums[start])) {
            return true;
        }

        return groupSumClump(start + 1, nums, target);
    }
}
