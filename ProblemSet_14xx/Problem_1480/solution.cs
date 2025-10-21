public class Solution
{
    public int[] RunningSum(int[] nums)
    {
        int n = nums.Length;
        int[] result = new int[n];
        
        if (n == 0) return result;

        result[0] = nums[0];
        for (int i = 1; i < n; i++)
        {
            result[i] = result[i - 1] + nums[i];
        }

        return result;
    }
}