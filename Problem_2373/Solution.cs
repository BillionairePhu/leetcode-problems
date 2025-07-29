namespace LeetCode;

[TestClass]
public class Solution_2373
{

    [TestMethod]
    public void SayHello()
    {
        List<int> list = new List<int>() { 1, 2, 3 };
        Console.WriteLine(list.Sum());
        Console.WriteLine(Math.Sqrt(10));
    }

    public int[][] LargestLocal(int[][] grid)
    {
        int n = grid.Length;
        int[][] result = new int[n - 2][];


        for (int i = 0; i < n - 2; i++)
        {
            result[i] = new int[n - 2]; // Must initialize the inner array

            for (int j = 0; j < n - 2; j++)
            {
                result[i][j] = FindMax(new int[]
                {
                    grid[i][j],     grid[i][j + 1],     grid[i][j + 2],
                    grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                    grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
                });
            }
        }

        return result;
    }

    public int FindMax(int[] values)
    {
        int max = values[0];
        for (int i = 1; i < values.Length; i++)
        {
            max = Math.Max(max, values[i]);
        }
        return max;
    }
}
