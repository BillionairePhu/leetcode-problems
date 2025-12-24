Solution s = new();
int[][] check = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]];
Console.WriteLine(s.CheckValidCutsHor(5,check,0,2));
Console.WriteLine(s.CheckValidCutsHor(5,check,1,3));

check = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]];
Console.WriteLine(s.CheckValidCutsHor(4,check,0,2));
Console.WriteLine(s.CheckValidCutsHor(4,[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]],1,3));

check = [[1,0,5,1],[0,2,2,4],[3,2,5,3],[0,4,4,5]];
Console.WriteLine(s.CheckValidCutsHor(5,check,0,2));
Console.WriteLine(s.CheckValidCutsHor(5,check,1,3));

public class Solution {
    public bool CheckValidCuts(int n, int[][] rectangles)
    {
        return CheckValidCutsHor(n, rectangles, 0, 2) || CheckValidCutsHor(n, rectangles, 1, 3);
    }
    public bool CheckValidCutsHor(int n, int[][] rectangles, int starthor, int endhor)
    {
        Array.Sort(rectangles, (a, b) => a[starthor] - b[starthor]);
        List<(int, int)> wherecannotcut = [(-1,-1)];
        for (int i = 0; i < rectangles.Length; i++)
        {
            var rect = rectangles[i];
            if (rect[starthor] + 1 < rect[endhor])
            {
                if (rect[starthor] + 1 <= wherecannotcut[^1].Item2)
                {
                    wherecannotcut[^1] = (wherecannotcut[^1].Item1, Math.Max(rect[endhor], wherecannotcut[^1].Item2));
                }
                else
                {
                    wherecannotcut.Add((rect[starthor]+1,rect[endhor]));
                }
            }
        }
        int last = 0;
        for (int i = 0; i < 3; i++)
        {
            int left = 0;
            int right = rectangles.Length -1;
            int index = -1;
            while (left <= right)
            {
                int mid = (left + right)/2;
                if (rectangles[mid][starthor] >= last)
                {
                    index = mid;
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            if (index == -1) return false;
            var cancutbeyond = rectangles[index][endhor];
            left = 0;
            right = wherecannotcut.Count -1;
            index = -1;
            while (left <= right)
            {
                int mid = (left + right)/2;
                if (wherecannotcut[mid].Item2 >= cancutbeyond)
                {
                    index = mid;
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            if (index == -1)
                last = cancutbeyond;
            else
            {
                if (cancutbeyond < wherecannotcut[index].Item1)
                    last = cancutbeyond;
                else
                    last = wherecannotcut[index].Item2;
            }
        }
        return true;
    }
}