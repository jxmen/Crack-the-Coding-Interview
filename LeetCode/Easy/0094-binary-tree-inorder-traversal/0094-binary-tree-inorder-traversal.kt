class Solution {

    // binary tree의 root가 주어지면 중위순회한 숫자들을 리턴하라. (중위순회: left -> root -> right)
    fun inorderTraversal(root: TreeNode?): List<Int> {
        if (root == null) return emptyList()
        
        val vals = mutableListOf<Int>()
        vals.addAll(inorderTraversal(root.left) ?: emptyList())
        vals.add(root.`val`)
        vals.addAll(inorderTraversal(root.right) ?: emptyList())
        
        return vals
    }
}
