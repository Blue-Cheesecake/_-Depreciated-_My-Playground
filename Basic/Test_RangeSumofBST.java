package Basic;

import java.util.LinkedList;
import java.util.Queue;

import Definition.TreeNode;

public class Test_RangeSumofBST {

    // ! use level order

    public int rangeSumBST(TreeNode root, int low, int high) {

        int sum = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();

        if (root != null) {
            q.add(root);
        }

        while (!q.isEmpty()) {

            TreeNode temp = q.poll();
            if (temp.val >= low && temp.val <= high) {
                sum += temp.val;
            }

            if (temp.left != null) {
                q.add(temp.left);
            }
            if (temp.right != null) {
                q.add(temp.right);
            }

        }

        return sum;
    }

    public static void main(String[] args) {

        TreeNode t = new TreeNode(1);
        t.left = new TreeNode(2);
        t.right = new TreeNode(3);
        t.left.left = new TreeNode(3);
        t.left.right = new TreeNode(5);
        t.right.right = new TreeNode(7);
        t.left.left.left = new TreeNode(5);

        Test_RangeSumofBST r = new Test_RangeSumofBST();
        System.out.println(r.rangeSumBST(t, 5, 10));
    }
}