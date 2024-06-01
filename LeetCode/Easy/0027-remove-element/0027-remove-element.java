class Solution {
    // k: nums에서 val을 제외한 값들의 개수
    // val: nums에서 제거할 숫자
    public int removeElement(int[] nums, int val) {
        
        // 1. two pointer로 제거할 숫자는 맨 오른쪽부터해서 위치시킨다.
        // p2는 맨 오른쪽에서 시작하며, 지울 숫자를 발견하면 p1의 있는 숫자와 스왑하고 p2 숫자는 왼쪽으로 이동시킨다.
        int p1 = 0, p2 = nums.length - 1;
        while (p1 <= p2) {
            if (nums[p1] == val && nums[p2] == val) {
                p2--;
                continue;
            }
            
            if (nums[p1] == val) {
                nums = swap(nums, p1, p2);
                p2--;
            }
            
            p1++;
        }
        
        // 3. nums에서 맨 앞의 k만큼의 개수를 리턴한다.
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) return k;
            k++;
        }
        
        return k;
    }
    
    private int[] swap(int[] nums, int p1, int p2) {
        int temp = nums[p1];
        nums[p1] = nums[p2];
        nums[p2] = temp;
        
        return nums;
    }
    
}