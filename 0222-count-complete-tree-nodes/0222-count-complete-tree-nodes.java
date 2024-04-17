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
    public int countNodes(TreeNode root) {
        return countNodesHelp(root, 0);
    }
    
    private int countNodesHelp(TreeNode root, int count) {
        if (root == null) return count;
        
        return 1 + countNodesHelp(root.left, count) 
            + countNodesHelp(root.right, count);
    }
}