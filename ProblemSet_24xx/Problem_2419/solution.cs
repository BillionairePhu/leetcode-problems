namespace LeetCode.ProblemSet_24;

[TestClass]
public class Solution_2419
{
    public int LongestSubarray(int[] nums)
    {
        int largest = 0;
        int max = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] > max)
            {
                max = nums[i];
                largest = 0;
            }
            if (nums[i] == max)
            {
                int j;
                for (j = i + 1; j < nums.Length && nums[j] == max; j++) ;
                largest = Math.Max(largest, j - i);
                // Compensate for i++
                i = j - 1;
            }
        }
        return largest;
    }
}
