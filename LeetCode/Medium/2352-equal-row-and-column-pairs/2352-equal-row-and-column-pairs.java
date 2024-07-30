import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.IntStream;

class Solution {
	public int equalPairs(int[][] grid) {
		int count = 0;

		// row 하나를 잡고, 그 row에 있는 숫자들의 개수를 저장하는 arraylist를 만든다.
		List<Integer> rowNums = new ArrayList<>();
		for (int[] row : grid) {

			// row에 있는 숫자들을 넣는다.
			Arrays.stream(row).forEach(rowNums::add);

			// 열을 모두 돌면서 저장한다.
			for (int i = 0; i < row.length; i++) {
				List<Integer> columnNums = new ArrayList<>();
				for (int j = 0; j < row.length; j++) {
					columnNums.add(grid[j][i]);
				}

				boolean isMatch = IntStream.range(0, rowNums.size())
						.allMatch(index -> Objects.equals(rowNums.get(index), columnNums.get(index)));
				if (isMatch) count++;
				columnNums.clear();
			}

			rowNums.clear();
		}

		return count;
	}
}
