class Solution {

    public int majorityElement(int[] nums) {
      // majority element가 있기 때문에 이 알고리즘 풀이가 가능하다. (Boyer-Moore Majority Vote Algorithm) 과반수 투표 알고리즘
      int majority = 0, count = 0;

      for (int num : nums) {
        /** count가 0이 되었다면 majority 후보가 바뀐다. */
        if (count == 0) {
          majority = num; 
          count = 1;
        } else if (num == majority) {
          count++;
        } else {
          count--;
        }
      }

      return majority;
    }

    // Follow-up: Could you solve the problem in linear time and in O(1) space?
    public int majorityElement2(int[] nums) {
      int majority = 0, count = 0;

      for (int i = 1; i < nums.length; i++) {
        if (count == 0) {
          majority = nums[i];
          count = 1;
          continue;
        }

        if (nums[i] == majority) {
          count++;
          continue;
        }

        count--;
        int iCount = findCount(nums, nums[i]); // findCount
        if (iCount > count) {
          majority = nums[i];
          count = iCount;
        }
      }

      return majority;
    }

    private int findCount(int[] nums, int target) {
      int count = 0;
      for (int num : nums) {
        if (num == target) count++;
      }

      return count;
    }
}
