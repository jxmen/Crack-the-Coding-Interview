import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
	public int minSwaps(int[] nums) {
		int n = nums.length;

		// 1의 개수를 센다 - 슬라이딩 윈도우 크기로 사용
		int ones = (int) Arrays.stream(nums).filter(num -> num == 1).count();

		// 윈도우 내 0의 개수를 센다
		int zerosInWindow = (int) IntStream.range(0, ones).filter(i -> nums[i] == 0).count();
		int minSwaps = zerosInWindow;

		// 슬라이딩 윈도우 이동
		for (int i = 1; i < n; i++) {
			// % 연산자를 통해 인덱스를 구해서 0인지 확인한다
			int outWindowIndex = (i - 1) % n;
			if (nums[outWindowIndex] == 0) {
				zerosInWindow--;
			}
			int inWindowIndex = (i + ones - 1) % n;
			if (nums[inWindowIndex] == 0) {
				zerosInWindow++;
			}
			minSwaps = Math.min(minSwaps, zerosInWindow);
		}

		return minSwaps;
	}
}
