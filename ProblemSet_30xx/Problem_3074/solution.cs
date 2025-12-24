Solution s = new();
Console.WriteLine(s.MinimumBoxes([1,3,2], [4,3,1,5,2]));


public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        int sum = apple.Sum();
        Array.Sort(capacity);
        int i;
        for (i = capacity.Length - 1; sum > 0 && i >= 0; i--)
        {
            sum -= capacity[i];
        }
        return capacity.Length - 1 - i;
    }
}