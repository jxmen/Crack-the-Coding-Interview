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
        return countNodeHelpOptimized(root);
    }
    
    private int countNodesHelp(TreeNode root, int count) {
        if (root == null) return count;
        
        return 1 + countNodesHelp(root.left, count) 
            + countNodesHelp(root.right, count);
    }
    
    // O(logN * logN) 으로 최적화한 버전
    private int countNodeHelpOptimized(TreeNode root) {
        if (root == null) return 0;
        
        // O(log N)
        int leftDepth = getDepth(root.left);
        int rightDepth = getDepth(root.right);
        
        // 왼쪽이 완전 이진트리일 경우 leftDepth^2 + rightCount
        if (leftDepth == rightDepth) {
            return (int) Math.pow(2, leftDepth) + countNodeHelpOptimized(root.right);
        } else {
            return (int) Math.pow(2, rightDepth) + countNodeHelpOptimized(root.left);
        }
    }
    
    private int getDepth(TreeNode root) {
        if (root == null) return 0;
        
        return 1 + getDepth(root.left);
    }
}