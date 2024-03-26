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
        TreeNode parent = this.findParentOf(val, root);
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
    
    // val이 들어갈 위치 할당을 위해 부모를 먼저 찾는다. val보다 큰 값을 찾을때까지 반복한다.
    private TreeNode findParentOf(int val, TreeNode node) {
        TreeNode parent = null;
        while (node != null) {
            parent = node;
            if (val > node.val) {
                node = node.right;
            } else if (val < node.val) {
                node = node.left;
            }
        }
        
        return parent;
    }
}