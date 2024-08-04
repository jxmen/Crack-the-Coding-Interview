import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
	public int rangeSum2(int[] nums, int n, int left, int right) {
		List<Long> subArraySums = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			long sum = 0;
			for (int j = i; j < n; j++) {
				sum += nums[j];
				subArraySums.add(sum);
			}
		}

		subArraySums.sort(Long::compareTo);
		long result = subArraySums.subList(left - 1, right)
				.stream()
				.reduce(0L, Long::sum);

		// 모듈로 연산을 사용하여 결과가 int 범위 내에 들어가도록 합니다.
		return (int) (result % 1_000_000_007);
	}

	// 최소 힙으로 결과 최적화 버전
	public int rangeSum(int[] nums, int n, int left, int right) {
		PriorityQueue<Long> minHeap = new PriorityQueue<>();
		for (int i = 0; i < n; i++) {
			long sum = 0;
			for (int j = i; j < n; j++) {
				sum += nums[j];
				minHeap.offer(sum);
			}
		}

		long result = 0;
		for (int i = 1; i <= right; i++) {
			Long currentSum = minHeap.poll();
			if (i >= left) {
				// 모듈로 연산을 사용하여 결과가 int 범위 내에 들어가도록 합니다.
				result = (result + currentSum) % 1_000_000_007;
			}
		}

		return (int) result;
	}

}
