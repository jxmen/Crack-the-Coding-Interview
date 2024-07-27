class Solution {
	public String[] findRelativeRanks(int[] score) {
		// 1. scoreMap hashMap을 만든다.
		Map<Integer, Integer> scoreMap = new HashMap<>();

		// 2. 최대 힙을 만들고, score를 모두 넣는다.
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
		Arrays.stream(score).forEach(maxHeap::add);

		// 3. 최대 힙에서 하나씩 꺼내면서 map에 넣는다.
		int size = maxHeap.size();
		for (int rank = 1; rank <= size; rank++) {
			Integer polled = maxHeap.poll();
			scoreMap.put(polled, rank);
		}

		// 4. socre를 돌면서 map에 있는 값을 조회하여 array에 담는다.
		return Arrays.stream(score)
				.map(scoreMap::get)
				.mapToObj(rank ->
						switch (rank) {
							case 1 -> "Gold Medal";
							case 2 -> "Silver Medal";
							case 3 -> "Bronze Medal";
							default -> String.valueOf(rank);
						}
				).toArray(String[]::new);
	}
}
