import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
	public boolean canBeEqual(int[] target, int[] arr) {
		Map<Integer, Integer> map = new HashMap();
		Arrays.stream(target).forEach(it -> {
			map.put(it, map.getOrDefault(it, 0) + 1);
		});

		for (int i : arr) {
			if (!map.containsKey(i)) {
				return false;
			}

			map.put(i, map.get(i) - 1);
		}

		return map.values().stream()
				.allMatch(it -> it == 0);
	}
}
