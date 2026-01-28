using System.Text;
Solution s = new Solution();
System.Console.WriteLine(s.LargestNumber([3,30,34,5,9]));


public class Solution {
    public string LargestNumber(int[] nums) {
        StringBuilder sb = new();
        string[] nstring = new string[nums.Length];
        for (int i = 0; i < nums.Length; i++)
        {
            nstring[i] = nums[i].ToString();
        }
        Array.Sort(nstring, new NumberStringComparer());
        if (nstring[^1] == "0") return "0";
        for (int i = nums.Length - 1; i >= 0; i--)
        {
            sb.Append(nstring[i]);
        }
        return sb.ToString();
    }
}

public class NumberStringComparer : IComparer<string>
{
    public int Compare(string x, string y)
    {
        return (x + y).CompareTo(y + x);
    }
}
