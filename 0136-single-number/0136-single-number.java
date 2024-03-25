import java.util.HashMap;
import java.util.Map;

class Solution {
	public int singleNumber(int[] nums) {
		Map<Integer, Integer> map = new HashMap<>();

		for (int num: nums) {
			if (map.get(num) == null) {
				map.put(num, 1);
			} else {
				map.put(num, map.get(num) + 1);
			}
		}

		for (int key: map.keySet()) {
			if (map.get(key) == 1) {
				return key;
			}
		}

		throw new IllegalStateException("No single number found");
	}
}