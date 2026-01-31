public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        Array.Sort(nums);
        if (k <= 1) return 0;
        k -= 1;
        int min = int.MaxValue;
        for (int i = 0; i + k < nums.Length; i++)
        {
            min = Math.Min(min, nums[i + k] - nums[i]);
        }
        return min;
    }
}