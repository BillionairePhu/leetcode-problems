Solution s = new();
Console.WriteLine(s.MaxDotProduct([3,-1,0],[4,5,3]));

public class Solution {
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int[] dp = new int[nums2.Length];
        for (int i = 0; i < nums1.Length; i++)
        {
            for (int j = dp.Length - 1; j >= 1 ; j--)
            {
                dp[j] = Math.Max(dp[j], dp[j - 1] + nums1[i] * nums2[j]);
            }
            dp[0] = Math.Max(dp[0], nums1[i] * nums2[0]);
            for (int j = 1; j < dp.Length; j++)
            {
                dp[j] = Math.Max(dp[j], dp[j - 1]);
            }
        }
        int max = dp[^1];
        if (max == 0)
        {
            max = nums1[0] * nums2[0];
            for (int i = 0; i < nums1.Length; i++)
            {
                for (int j = 0; j < nums2.Length; j++)
                {
                    max = Math.Max(max, nums1[i] * nums2[j]);
                }
            }
            return max;
        }
        return max;
    }
}