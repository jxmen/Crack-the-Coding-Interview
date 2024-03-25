import java.util.HashMap;
import java.util.Map;

class Solution {
	public int singleNumber(int[] nums) {
		Map<Integer, Integer> map = new HashMap<>();

		for (int num: nums) {
            // key가 없을 경우 1로 초기화
			map.merge(num, 1, Integer::sum);
		}

		return map.keySet().stream()
				.filter(key -> map.get(key) == 1)
				.findFirst()
				.orElseThrow(IllegalStateException::new);
	}
}
