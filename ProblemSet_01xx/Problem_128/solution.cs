Solution s = new();
Console.WriteLine(s.LongestConsecutive([100,4,200,1,3,2]));


public class Solution {
    public class Range(int Start, int End)
    {
        public int Start = Start;
        public int End = End;
    }
    public int LongestConsecutive(int[] nums) {
        Dictionary<int, Range> dict = new Dictionary<int, Range>();
        if (nums.Length == 0) return 0;
        int longest = 1;
        foreach (var n in nums)
        {
            if (dict.TryAdd(n, new Range(n, n)))
            {
                if (dict.TryGetValue(n - 1, out var rangeleft))
                {
                    if (dict.TryGetValue(n + 1, out var rangeright))
                    {
                        longest = Math.Max(longest, rangeright.End - rangeleft.Start + 1);
                        dict[rangeleft.Start].End = rangeright.End;
                        dict[rangeright.End].Start = rangeleft.Start;
                    }
                    else
                    {
                        longest = Math.Max(longest, n - rangeleft.Start + 1);
                        dict[rangeleft.Start].End = n;
                        dict[n].Start = rangeleft.Start;
                    }
                }
                else
                {
                    if (dict.TryGetValue(n + 1, out var rangeright))
                    {
                        longest = Math.Max(longest, rangeright.End - n + 1);
                        dict[rangeright.End].Start = n;
                        dict[n].End = rangeright.End;
                    }
                }
            }
        }
        return longest;
    }
}