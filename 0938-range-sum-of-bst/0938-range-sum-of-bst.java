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
    
    // low <= val <= high 를 충족할 경우의 총합 리턴
    public int rangeSumBST(TreeNode root, int low, int high) {
        // low와 high 값을 이용할 수 없을까?
        if (root == null) {
            return 0;
        }
        
        int sum = 0;
        if (low <= root.val && root.val <= high) {
            sum += root.val;
        }
        
        int leftSum = rangeSumBST(root.left, low, high);
        int rightSum = rangeSumBST(root.right, low, high);
        
        return sum + leftSum + rightSum;
    }
}