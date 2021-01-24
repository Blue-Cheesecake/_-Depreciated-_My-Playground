package Intermediete;

import Definition.TreeNode;
import java.util.List;
import java.util.ArrayList;

class Test_BinaryTreePostOrder {

    public void helper(TreeNode cur, List<Integer> arr) {

        if (cur == null) {
            return;
        }

        helper(cur.left, arr);
        helper(cur.right, arr);
        arr.add(cur.val);

    }

    public List<Integer> postorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<Integer>();
        helper(root, result);
        return result;

    }
}