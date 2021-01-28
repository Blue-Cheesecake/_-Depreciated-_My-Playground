package Basic;

import Definition.TreeNode;
import java.util.Queue;
import java.util.LinkedList;

public class Test_SearchinaBinarySearchTree {

    public TreeNode searchBST(TreeNode root, int val) {

        Queue<TreeNode> q = new LinkedList<TreeNode>();

        if (root != null) {

            q.add(root);

            while (!q.isEmpty()) {

                TreeNode temp = q.poll();
                if (temp.val == val) {
                    return temp;
                }
                if (temp.left != null) {
                    q.add(temp.left);
                }
                if (temp.right != null) {
                    q.add(temp.right);
                }
            }
        }

        return null;
    }

}
