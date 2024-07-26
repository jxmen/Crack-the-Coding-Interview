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

				int[] newRow = new int[row.length - 1];
				for (int j = 0; j < newRow.length; j++) {
					newRow[j] = maxHeap.poll();
				}

				grid[i] = newRow;
			}

			sum += gridMax;
		}

		return sum;
	}
}


