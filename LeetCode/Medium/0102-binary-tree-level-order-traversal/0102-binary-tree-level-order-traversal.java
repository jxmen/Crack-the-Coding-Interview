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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return List.of();
        
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> answer = new ArrayList<>();
        queue.offer(root);
        
        while(!queue.isEmpty()) {
            List<Integer> nums = new ArrayList<>();
            
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode polled = queue.poll();
                nums.add(polled.val);
                
                if (polled.left != null) {
                    queue.offer(polled.left);
                }
                
                if (polled.right != null) {
                    queue.offer(polled.right);
                }
            }
            
            answer.add(nums);
        }
        
        
        return answer;
    }
    
    
}