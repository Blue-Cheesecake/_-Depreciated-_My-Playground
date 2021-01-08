package Basic;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class LastStoneWeight {

    // ! find 1st and 2nd largest
    public List<Integer> getMax(List<Integer> arr) {

        Collections.sort(arr);
        return arr;

    }

    public int lastStoneWeight(int[] stones) {

        List<Integer> result = new ArrayList<Integer>();

        for (int i = 0; i < stones.length; i++) {
            result.add(stones[i]);
        }

        while (result.size() > 1) {

            Collections.sort(result);
            int n = result.size();
            int first = result.get(n - 1);
            int second = result.get(n - 2);

            result.remove(n - 1);
            result.remove(n - 2);

            if (first == second) {
                continue;
            }

            result.add(first - second);

        }

        if (result.size() == 0) {
            return 0;
        }
        return result.get(0);
    }

    public static void main(String[] args) {
        LastStoneWeight sol = new LastStoneWeight();
        int[] t1 = { 2, 7, 4, 1, 8, 1, 5, 6, 8, 4, 1, 2, 3, 6, 15, 8, 4, 5, 6 };
        System.out.println(sol.lastStoneWeight(t1));
    }
}
