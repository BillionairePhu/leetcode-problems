public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);
        List<IList<int>> res = [];
        int min = int.MaxValue;
        for (int i = 0; i < arr.Length - 1; i++)
        {
            if (arr[i + 1] - arr[i] < min)
            {
                res = [[arr[i], arr[i + 1]]];
                min = arr[i + 1] - arr[i];
            }
            else if (arr[i + 1] - arr[i] == min)
            {
                res.Add([arr[i], arr[i + 1]]);
            }
        }
        return res;
    }
}