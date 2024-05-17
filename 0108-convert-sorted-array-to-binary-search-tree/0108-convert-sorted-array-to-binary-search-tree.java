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
      
    // divide and conquer 방식으로 풀어보자.
    public TreeNode sortedArrayToBST(int[] nums) {
      if (nums.length == 0) return null; 
      if (nums.length == 1) return new TreeNode(nums[0]);

      /**
       * 중간값을 찾고 해당 배열에서 왼쪽을 BST로 만든 뒤 또 연결하고, 오른쪽도 BST로 만든 후 연결하고 만든 TreeNode를 리턴한다.
       * 예를 들어 [1,2,3] 이라는 값이 주어진다면, 중간값인 2가 root가 되고 1이 left, 3이 right가 된다.
       *
       * Find the middle value and create a BST from the left part of the array and connect it, then create a BST from the right part and connect it, and return the created TreeNode.
       * For example, if the input is [1, 2, 3], the middle value 2 becomes the root, 1 becomes the left, and 3 becomes the right.
       */
      int middleIndex = nums.length / 2;
      TreeNode root = new TreeNode(nums[middleIndex]);
      root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, middleIndex));
      root.right = sortedArrayToBST(Arrays.copyOfRange(nums, middleIndex + 1, nums.length));

      return root;
    }
}
