package Basic;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import Definition.TreeNode;

public class Test_IncreasingOrderSearchTree {

    public void helper(TreeNode cur, List<Integer> arr) {

        if (cur == null) {
            return;
        }

        helper(cur.left, arr);
        arr.add(cur.val);
        helper(cur.right, arr);

    }

    public List<Integer> inorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<Integer>();
        helper(root, result);
        return result;

    }

    public TreeNode increasingBST(TreeNode root) {

        TreeNode result = new TreeNode();
        List<Integer> arr = inorderTraversal(root);
        Collections.sort(arr);
        TreeNode travel = result;
        boolean first = true;

        for (int i = 0; i < arr.size(); i++) {

            TreeNode newNode = new TreeNode(arr.get(i));

            if (first) {
                first = false;
                result = newNode;
                travel = result;
                continue;
            }

            travel.right = newNode;
            travel = travel.right;
        }

        return result;
    }

    public static void main(String[] args) {

        TreeNode t = new TreeNode(1);
        t.left = new TreeNode(2);
        t.right = new TreeNode(3);
        t.left.left = new TreeNode(10);
        t.left.right = new TreeNode(5);
        t.right.left = new TreeNode(8);
        t.right.right = new TreeNode(9);
        t.left.left.left = new TreeNode(4);
        t.left.left.right = new TreeNode(16);
        t.right.left.left = new TreeNode(12);
        t.right.left.right = new TreeNode(7);

        Test_IncreasingOrderSearchTree r = new Test_IncreasingOrderSearchTree();
        System.out.println(r.increasingBST(t));
    }
}