public class Solution {
    public int MinRemoval(int[] nums, int k) {
        Array.Sort(nums);
        int left = 0;
        int right = 1;
        int maxlength = 1;
        while (left < nums.Length)
        {
            while (right < nums.Length && (long)nums[right] <= (long)k * nums[left]) right++; // remember to avoid int overflow
            maxlength = Math.Max(maxlength, right - left);
            left++;
        }
        return nums.Length - maxlength;
    }
}