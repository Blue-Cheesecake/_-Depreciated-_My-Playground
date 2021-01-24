package Intermediete;

import Definition.TreeNode;
import java.util.List;
import java.util.ArrayList;

public class Test_BinaryTreeInOrder {

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

}