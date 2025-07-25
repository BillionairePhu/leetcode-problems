namespace LeetCode;
public class Solution1695
{
    public int MaximumUniqueSubarray(int[] nums)
    {
        HashSet<int> found = new();
        int max = 0;
        int sum = 0;
        int start = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (found.Contains(nums[i]))
            {
                for (; nums[start] != nums[i]; start++)
                {
                    sum -= nums[start];
                    found.Remove(nums[start]);
                }
                start++;
            }
            else
            {
                sum += nums[i];
                max = Math.Max(sum, max);
                found.Add(nums[i]);
            }
        }
        return max;
    }
}