class Solution {
    public int maxProduct(int[] nums) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        Arrays.stream(nums).forEach(maxHeap::offer);

        int first = maxHeap.poll();
        int second = maxHeap.poll();
        return (first - 1) * (second - 1);
    }
}