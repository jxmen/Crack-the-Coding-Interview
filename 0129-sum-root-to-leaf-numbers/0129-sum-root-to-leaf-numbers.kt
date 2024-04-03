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

fun TreeNode.hasChild(): Boolean {
    return this.left != null || this.right != null
}

class Solution {
    fun sumNumbers(root: TreeNode?): Int {
        if (root == null) return 0
        
        // 자식의 문자열 목록들을 모두 받아와서 sum에 합치고 리턴한다.
        val list = getChildStrs(root)
        return list.map { it -> it.toInt() }.sum()
    }
    
    private fun getChildStrs(root: TreeNode?): List<String> {
        if (root == null) return emptyList()
        
        if (!root.hasChild()) {
            return listOf(root.`val`.toString())
        }
        
        // 자식들의 리스트를 얻어서 합친다.
        val left = getChildStrs(root.left)
        val right = getChildStrs(root.right)
        
        return listOf(left, right).flatten()
            .map { it -> root.`val`.toString() + it }
    }
}