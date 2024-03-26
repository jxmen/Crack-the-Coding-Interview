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

    // 삽입 후에도 BST를 유지하고 root를 리턴한다.
    public TreeNode insertIntoBST(TreeNode root, int val) {
        
        // val이 들어갈 자리를 찾는다. val보다 큰 값을 찾을때까지 반복한다.
        TreeNode node = root;
        TreeNode parent = null;
        while (node != null) {
            if (val > node.val) {
                parent = node;
                node = node.right;
            } else if (val < node.val) {
                parent = node;
                node = node.left;
            }
        }
        
        if (parent == null) {
            root = new TreeNode(val);
            return root;
        }
        
        if (val > parent.val) {
            parent.right = new TreeNode(val);
        } else if (val < parent.val) {
            parent.left = new TreeNode(val);
        }
        
        return root;
    }
}