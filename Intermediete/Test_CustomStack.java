class CustomStack {

    Integer[] stack;
    int iCur;

    public CustomStack(int maxSize) {

        stack = new Integer[maxSize];

        if (maxSize > 0) {
            iCur = 0;
        } else {
            iCur = -1;
        }

    }

    public void push(int x) {

        if (stack.length < 1) {
            return;
        }

        if (iCur < stack.length) {

            stack[iCur] = x;
            iCur++;

        }

    }

    public int pop() {

        if (iCur - 1 >= 0) {

            iCur--;
            int ret = stack[iCur];
            stack[iCur] = null;
            return ret;

        }

        return -1;
    }

    public void increment(int k, int val) {

        int n = k;

        if (k > stack.length) {
            n = stack.length;
        }

        for (int i = 0; i < n; i++) {

            if (stack[i] == null) {
                break;
            }
            stack[i] += val;

        }

    }
}

/**
 * Your CustomStack object will be instantiated and called as such: CustomStack
 * obj = new CustomStack(maxSize); obj.push(x); int param_2 = obj.pop();
 * obj.increment(k,val);
 */

public class Test_CustomStack {

    public static void main(String[] args) {

        CustomStack object = new CustomStack(3);
        object.push(1);
        object.push(2);
        System.out.println(object.pop());
        object.push(2);
        object.push(3);
        object.push(4);
        object.increment(5, 100);
        object.increment(2, 100);
        System.out.println(object.pop());
        System.out.println(object.pop());
        System.out.println(object.pop());
        System.out.println(object.pop());

    }
}