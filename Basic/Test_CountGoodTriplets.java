
package Basic;

// https://leetcode.com/problems/count-good-triplets/

public class Test_CountGoodTriplets {

    // |arr[i] - arr[j]| <= a
    // |arr[j] - arr[k]| <= b
    // |arr[i] - arr[k]| <= c

    public int countGoodTriplets(int[] arr, int a, int b, int c) {

        int n = arr.length;
        int count = 0;

        for (int i = 0; i < n - 2; i++) {

            for (int j = i + 1; j < n - 1; j++) {

                for (int k = j + 1; k < n; k++) {

                    int suspectA = Math.abs(arr[i] - arr[j]);
                    int suspectB = Math.abs(arr[j] - arr[k]);
                    int suspectC = Math.abs(arr[i] - arr[k]);

                    if (suspectA <= a && suspectB <= b && suspectC <= c) {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] arr = { 3, 0, 1, 1, 9, 7 };
        Test_CountGoodTriplets Solution = new Test_CountGoodTriplets();
        System.err.println(Solution.countGoodTriplets(arr, 7, 2, 3));
    }
}
