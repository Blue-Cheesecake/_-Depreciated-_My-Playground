// https://leetcode.com/problems/maximum-depth-of-binary-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public int findMacDeep(TreeNode root, int currMax) {

        if (root == null) {
            return currMax;
        }

        int n1 = findMacDeep(root.left, currMax + 1);
        int n2 = findMacDeep(root.right, currMax + 1);

        if (n1 >= n2) {
            return n1;
        }
        return n2;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return findMacDeep(root, 0);
    }
}
