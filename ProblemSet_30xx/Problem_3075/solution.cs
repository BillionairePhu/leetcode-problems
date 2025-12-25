Solution s = new();
Console.WriteLine(s.MaximumHappinessSum([2,3,4,5],2));

public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);
        long max = 0;
        int negcompensation = 0;
        for (int i = happiness.Length - 1; i >= 0; i--)
        {
            if (k <= 0)
                return max;
            k--;
            if (happiness[i] <= negcompensation)
                return max;
            max += happiness[i] - negcompensation;
            negcompensation++;
        }
        return max;
    }
}