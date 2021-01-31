public class Test_SumofAllOddLengthSubarrays {

    public int sumOddLengthSubarrays(int[] arr) {

        int len = 1;
        int n = arr.length;
        int result = 0;

        while (len <= n) {

            for (int i = 0; i < n - len + 1; i++) {

                int count = 0;

                for (int j = i; j < len + i; j++) {

                    count += arr[j];

                }

                result += count;

            }

            len += 2;
        }

        return result;
    }

}