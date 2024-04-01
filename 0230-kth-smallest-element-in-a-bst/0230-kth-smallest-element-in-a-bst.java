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
    
    public List<Integer> getPreOrderValues() {
        if (this == null) return List.of();
        
        List<Integer> integers = new ArrayList<>();
        
        // left
        List<Integer> leftValues = Optional.ofNullable(this.left)
            .map(it -> it.getPreOrderValues())
            .orElse(List.of());
        integers.addAll(leftValues);

        // root
        integers.add(this.val);

        // right
        List<Integer> rightValues = Optional.ofNullable(this.right)
            .map(it -> it.getPreOrderValues())
            .orElse(List.of());
        integers.addAll(rightValues);
        
        return integers;
    }
}


class Solution {
    
    // k번째로 작은 숫자를 찾아 리턴하라. (k=1일 경우 가장 작은 숫자이다.)
    public int kthSmallest(TreeNode root, int k) {
        
        // bst의 값들을 정렬된 array로 만들고 k-1 인덱스에 접근
        List<Integer> preOrderIntegers = root.getPreOrderValues();
        
        return preOrderIntegers.get(k-1);
    }
    
    
}