class Solution {
	public int deleteGreatestValue(int[][] grid) {
		int sum = 0;

		// row에 요소가 하나도 없다면 종료
		while (grid[0].length != 0) {
			// row별로 최대값을 찾고 제거한다. 그리고 grid에서도 최대값은 sum에 추가한다.
			int gridMax = 0;
			for (int i = 0; i < grid.length; i++) {
				int[] row = grid[i];

				// 최대값을 찾는다.
				PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
				Arrays.stream(row).forEach(maxHeap::offer);
				int rowMax = maxHeap.poll(); // 최대값 제거
				gridMax = Math.max(gridMax, rowMax);

                // 최대값을 제외한 값을 array로 변환 후 다시 할당한다.
                // !! 스트림만 사용시에는 순서가 보장되지 않으나, 문제 특성상 순서가 보장되지 않아도 된다.
				grid[i] = maxHeap.stream()
                    .mapToInt(Integer::intValue)
                    .toArray();
			}

			sum += gridMax;
		}

		return sum;
	}
}


