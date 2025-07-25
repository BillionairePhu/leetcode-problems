namespace LeetCode;

public class Solution3487
{
    public int MaxSum(int[] nums)
    {
        HashSet<int> found = [];
        int sum = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] > 0 && found.Add(nums[i]))
            {
                sum += nums[i];
            }
        }
        return found.Count != 0 ? sum : nums.Min();
    }
}