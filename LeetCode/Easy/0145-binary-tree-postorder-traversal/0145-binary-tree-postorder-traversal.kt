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
    fun postorderTraversal(root: TreeNode?): List<Int> {
        if (root == null) return emptyList()
        
        val list = mutableListOf<Int>();
        list.addAll(postorderTraversal(root.left))
        list.addAll(postorderTraversal(root.right))
        list.add(root.`val`)
        
        return list
    }
}