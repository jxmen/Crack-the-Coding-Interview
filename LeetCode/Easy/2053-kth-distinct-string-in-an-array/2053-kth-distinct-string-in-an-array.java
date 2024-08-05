import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
	public String kthDistinct(String[] arr, int k) {
		Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
		Arrays.stream(arr).forEach(s -> linkedHashMap.put(s, linkedHashMap.getOrDefault(s, 0) + 1));

		// array를 돌면서 key의 value가 하나인 것 중 k번째 key 리턴
		for (String s: arr) {
			if (linkedHashMap.get(s) == 1) {
				if (k == 1) {
					return s;
				}
				k--;
			}
		}

		return "";
	}
}
