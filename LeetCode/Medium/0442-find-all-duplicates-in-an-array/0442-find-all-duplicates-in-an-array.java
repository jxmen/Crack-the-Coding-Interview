import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

class Solution {
	public List<Integer> findDuplicates(int[] nums) {
		// n 길이의 nums 정수 배열이 주어질 때, nums는 [1,n]의 길이를 가지고 있고 1번 혹은 2번 포함되어 있다.
		// 반환해라 배열의 정수가 2번 나타나는 숫자들을 배열에 포함하여
		// 시간복잡도: O(N)
		List<Integer> answers = new ArrayList<>();
		Set<Integer> set = new HashSet<>();
		for (int num: nums) {
			if (set.contains(num)) {
				answers.add(num);	
			} else {
				set.add(num);
			}
		}
		
		return answers;
	}
}