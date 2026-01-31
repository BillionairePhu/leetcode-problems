public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int max = int.MinValue;
        for (int i = 0; i < nums.Length / 2; i++)
        {
            max = Math.Max(max, nums[i] + nums[^(i + 1)]);
        }
        return min;
    }
}