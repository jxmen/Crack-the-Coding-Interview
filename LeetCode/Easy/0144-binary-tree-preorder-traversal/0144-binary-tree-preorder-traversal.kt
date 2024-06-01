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
    fun preorderTraversal(root: TreeNode?): List<Int> {
        if (root == null) return emptyList()
        
        val list = mutableListOf<Int>();
        list.add(root.`val`)
        list.addAll(preorderTraversal(root.left))
        list.addAll(preorderTraversal(root.right))
        
        return list
    }
}