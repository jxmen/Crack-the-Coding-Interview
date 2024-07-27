class Solution {
	public int minimumOperations(int[] nums) {
		int minimumOperations = 0;

		// 1. 최소 힙을 만든다.
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();

		// 2. nums에서 0이 아닌 값들을 모두 최소 힙에 넣는다.
		Arrays.stream(nums).filter(it -> it != 0).forEach(minHeap::offer);

		while (!minHeap.isEmpty()) {
			// 3. 최소 힙에서 값 하나를 꺼낸다.
			Integer min = minHeap.poll();

			// 4. operation 수 증가
			minimumOperations++;

			// 5. 힙에서 모든 값들을 꺼내고 최소 값을 빼고 다시 넣는다.
			List<Integer> arr = new ArrayList<>();
			IntStream.range(0, minHeap.size())
					.map(it -> minHeap.poll())
					.map(it -> it - min)
					.filter(it -> it != 0)
					.forEach(arr::add);

			arr.forEach(minHeap::offer);
		}

		return minimumOperations;
	}
}
