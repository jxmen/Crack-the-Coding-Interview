class Solution {
	public String frequencySort(String s) {
		Map<Character, Integer> countMap = new HashMap<>();
		for (char c : s.toCharArray()) {
			int count = countMap.getOrDefault(c, 0) + 1;
			countMap.put(c, count);
		}

		PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>((a, b) ->
				b.getValue() - a.getValue() // 개수가 많다면 큰 값으로 설정
		);
		for (Character c : countMap.keySet()) {
			pq.add(Map.entry(c, countMap.get(c)));
		}

		StringBuilder sb = new StringBuilder();
		while (!pq.isEmpty()) {
			Map.Entry<Character, Integer> polled = pq.poll();

			Character c = polled.getKey();
			Integer count = polled.getValue();

			IntStream.range(0, count).forEach(i -> sb.append(c));
		}

		return sb.toString();
	}
}
