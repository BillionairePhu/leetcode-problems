
namespace Problem_2411;

[TestClass]
public class Solution
{
    public Solution() { }

    [TestMethod]
    public void TestSolution()
    {
        int[] array = [1,0,2,1,3];
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
}
