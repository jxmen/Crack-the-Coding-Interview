public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
    
    public List<TreeNode> preOrderNodes() {
        if (this == null) return List.of();
        
        List<TreeNode> nodes = new ArrayList<>();
        
        // left
        List<TreeNode> leftNodes = Optional.ofNullable(this.left)
            .map(it -> it.preOrderNodes())
            .orElse(List.of());
        nodes.addAll(leftNodes);
        
        // root
        nodes.add(this);
            
        // right
        List<TreeNode> rightNodes = Optional.ofNullable(this.right)
            .map(it -> it.preOrderNodes())
            .orElse(List.of());
        nodes.addAll(rightNodes);
        
        return nodes;
    }
    
    public List<Integer> preOrderNodeFromInts() {
        if (this == null) return List.of();
        
        List<Integer> ints = new ArrayList<>();
        
        // left
        List<Integer> leftInts = Optional.ofNullable(this.left)
            .map(it -> it.preOrderNodeFromInts())
            .orElse(List.of());
        ints.addAll(leftInts);
        
        // root
        ints.add(this.val);
            
        // right
        List<Integer> rightInts = Optional.ofNullable(this.right)
            .map(it -> it.preOrderNodeFromInts())
            .orElse(List.of());
        ints.addAll(rightInts);
        
        return ints;
    }
}


class Solution {
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> ints = root.preOrderNodeFromInts();
        List<TreeNode> nodes = ints.stream().map(TreeNode::new).toList();
        
        TreeNode first = nodes.get(0);
        TreeNode prev = null;
        for (TreeNode node: nodes) {
            if (prev == null) {
                prev = node;
                continue;
            }
            
            prev.right = node;
            prev = node;
        }
        
        return first;
    }
}