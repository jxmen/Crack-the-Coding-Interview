class Solution {
	public int[] kWeakestRows(int[][] mat, int k) {
		// 가장 약한 행렬 k개의 인덱스 목록을 저장할 우선순위 큐
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
			// 행렬의 병사 수가 같다면 인덱스가 작은 순으로 정렬
			if (a[1] == b[1]) {
				return a[0] - b[0];
			}
			// 행렬의 병사 수가 적은 순으로 정렬
			return a[1] - b[1];
		});

		for (int index = 0; index < mat.length; index++) {
			int[] row = mat[index];

			pq.offer(new int[]{index, countOfSoldiers(row)});
		}

		return IntStream.range(0, k)
				.map(_ -> pq.poll()[0]) // 0: index, 1: count
				.toArray();
	}

	private int countOfSoldiers(int[] row) {
		int left = 0;
		int right = row.length - 1;
		while (left <= right) {
			int mid = left + (right - left) / 2;
			if (row[mid] == 1) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}

		return left;
	}
}