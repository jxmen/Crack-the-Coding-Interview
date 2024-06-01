/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxDepth(root: TreeNode?, depth: Int = 0): Int {
        if (root == null) return depth
        
        return Math.max(
            maxDepth(root.left, depth + 1), 
            maxDepth(root.right, depth + 1)
        )
    }
}