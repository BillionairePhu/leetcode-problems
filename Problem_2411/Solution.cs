using LeetCode.SolutionValidator;
namespace LeetCode;

[TestClass]
public class Solution_2411
{
    [TestMethod]
    public void TestSolution()
    {
        int[] array = [1, 0, 2, 1, 3];
        int[] result = SmallestSubarrays(array);
        foreach (int num in result)
        {
            Console.WriteLine(num);
        }
    }
    public int[] SmallestSubarrays(int[] nums)
    {
        int[] pos = Enumerable.Repeat(-1, 31).ToArray();
        int[] result = new int[nums.Length];
        for (int i = nums.Length - 1; i >= 0; i--)
        {
            for (int j = 0; j < pos.Length; j++)
            {
                if ((nums[i] & (1 << j)) != 0)
                {
                    pos[j] = i;
                }
            }
            int maxPos = pos.Max();
            if (maxPos > -1)
            {
                result[i] = maxPos - i + 1;
            }
            else
            {
                result[i] = 1;
            }
        }
        return result;
    }
    [SolutionValidator]
    public int[] SmallestSubarrays2nd(int[] nums)
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
