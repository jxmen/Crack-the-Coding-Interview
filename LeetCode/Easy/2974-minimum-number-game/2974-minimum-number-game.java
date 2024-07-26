class Solution {
	public int[] numberGame(int[] nums) {
		// init empty arr
		// alice와 bob은 라운드에서 하나를 옮김
		// 모든 라운드에서 alice는 가장 작은 값을 지움. 밥도 마찬가지
		// bob은 지운 값을 arr에 추가함. 앨리스도 마찬가지
		// nums가 빌때까지 반복

		List<Integer> integers = new ArrayList<>();

		// 두번 꺼내고, 두번째에 꺼낸거 먼저 넣고 그 다음 첫번째 꺼낸 것을 넣는다. 이를 계속 반복
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();
		Arrays.stream(nums).forEach(minHeap::offer);

		while (!minHeap.isEmpty()) {
			int first = minHeap.poll();
			int second = minHeap.poll();

			integers.add(second);
			integers.add(first);
		}

		return integers.stream()
            .mapToInt(Integer::intValue)
            .toArray();
	}
}
