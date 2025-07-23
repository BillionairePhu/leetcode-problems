public partial class Solution
{
    [TestMethod]
    public void MaximumUniqueSubarrayTest()
    {
        Assert.AreEqual(17, MaximumUniqueSubarray([4, 2, 4, 5, 6]));
        Assert.AreEqual(8, MaximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]));
    }
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