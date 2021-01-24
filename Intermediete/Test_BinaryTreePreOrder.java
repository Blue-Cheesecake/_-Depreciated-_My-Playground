package Intermediete;

import Definition.TreeNode;
import java.util.List;
import java.util.ArrayList;

public class Test_BinaryTreePreOrder {

    public void helper(TreeNode cur, List<Integer> arr) {

        if (cur != null) {
            arr.add(cur.val);
            helper(cur.left, arr);
            helper(cur.right, arr);
        }
    }

    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<Integer>();
        helper(root, result);
        return result;

    }
}