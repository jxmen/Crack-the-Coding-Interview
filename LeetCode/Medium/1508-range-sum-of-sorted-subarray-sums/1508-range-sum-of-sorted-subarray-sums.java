import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
	public int rangeSum(int[] nums, int n, int left, int right) {
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
}