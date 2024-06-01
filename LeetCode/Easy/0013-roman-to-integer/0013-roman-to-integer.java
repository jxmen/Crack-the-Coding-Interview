class Solution {

	// LinkedHashMap은 삽입할때의 순서가 보장됨
	private static final Map<String, Integer> romanMap = new LinkedHashMap<>();

	static {
		romanMap.put("M", 1000);
		romanMap.put("CM", 900);
		romanMap.put("D", 500);
		romanMap.put("CD", 400);
		romanMap.put("C", 100);
		romanMap.put("XC", 90);
		romanMap.put("L", 50);
		romanMap.put("XL", 40);
		romanMap.put("X", 10);
		romanMap.put("IX", 9);
		romanMap.put("V", 5);
		romanMap.put("IV", 4);
		romanMap.put("I", 1);
	}

	// 큰 숫자부터 Map을 만들고 문자열이 그것으로 시작하면 잘라내면서 sum에 더한다.
	public int romanToInt(String s) {
		return helper(s, 0);
	}

	private int helper(String s, int sum) {
		for (String key : romanMap.keySet()) {
			if (s.startsWith(key)) {
				String newStr = s.substring(key.length());
				return helper(newStr, sum + romanMap.get(key));
			}
		}
        
        return sum;
	}
}