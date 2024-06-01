class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1, k = m + n - 1;
        
        // p1은 앞에 숫자가 정렬되어 있으므로 p2만 벗어나면 종료한다.
        while (p2 >= 0) {
            // 더 큰 값을 nums1의 k 인덱스에 할당한다.
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[k--] = nums1[p1--];
            } else {
                nums1[k--] = nums2[p2--];
            }
        }
    }
}