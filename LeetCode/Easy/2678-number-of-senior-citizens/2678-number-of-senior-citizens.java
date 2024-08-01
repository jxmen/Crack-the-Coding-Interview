import java.util.Arrays;

class Solution {
	public int countSeniors(String[] details) {
		return (int) Arrays.stream(details)
				.mapToInt(detail -> Integer.parseInt(detail.substring(11, 13)))
				.filter(age -> age > 60)
				.count();
	}
}
