namespace LeetCode;

[TestClass]
public class Solution2441
{
    [TestMethod]
    public void SmallestSubarraysTest()
    {
        Console.WriteLine(string.Join(',', SmallestSubarrays([1, 0])));
    }
    public int[] SmallestSubarrays(int[] nums)
    {
        int[] res = new int[nums.Length];
        int[] lastseenbit = new int[30];
        for (int i = nums.Length - 1; i >= 0; i--)
        {
            int maxlast = i;
            for (int j = 0; j < 30; j++)
            {
                if (nums[i] % 2 == 1)
                {
                    lastseenbit[j] = i;
                }
                maxlast = Math.Max(lastseenbit[j], maxlast);
                nums[i] >>= 1;
            }
            res[i] = maxlast - i + 1;
        }
        return res;
    }
}