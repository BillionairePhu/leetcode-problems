public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        if (nums.Length < 2) return 0;
        
        int op = 0;
        PriorityQueue<DLink, MyPrio> pq = new();
        int decrease = 0;
        bool[] merged = new bool[nums.Length];
        DLink nilroot = new DLink(null, int.MinValue, -1);
        DLink last = nilroot;
        for (int i = 0; i < nums.Length - 1; i++)
        {
            last.Next = new DLink(last, nums[i], i);
            last = last.Next;
            pq.Enqueue(last, new MyPrio(nums[i] + nums[i + 1], i));
            if (nums[i] > nums[i + 1]) decrease++;
        }
        last.Next = new DLink(last, nums[nums.Length - 1], nums.Length - 1);
        last = last.Next;
        nilroot.Next.Prev = null;

        while (decrease > 0)
        {
            pq.TryDequeue(out var link, out var prio);
            if (merged[link.Index] || link.Next == null || merged[link.Next.Index] || link.Value + link.Next.Value != prio.Sum) continue;
            op += 1;

            DLink linkplus1 = link.Next;
            if (link.Value > linkplus1.Value) decrease--;
            DLink? linkplus2 = linkplus1.Next;

            if (linkplus2 != null)
            {
                if (linkplus1.Value > linkplus2.Value) decrease--;
                linkplus2.Prev = link;
                if (prio.Sum > linkplus2.Value) decrease++;
                pq.Enqueue(link, new MyPrio(prio.Sum + linkplus2.Value, link.Index));
            }
            merged[link.Next.Index] = true;
            link.Next = linkplus2;
            DLink? linkminus1 = link.Prev;

            if (linkminus1 != null)
            {
                if (linkminus1.Value > link.Value) decrease--;

                if (linkminus1.Value > prio.Sum) decrease++;
                pq.Enqueue(linkminus1, new MyPrio(linkminus1.Value + prio.Sum, linkminus1.Index));
            }
            link.Value = prio.Sum;
        }

        return op;
    }
}

[DebuggerDisplay("DLink({Value}, {Index}, {Ending})")]
public class DLink(DLink prev, long value, int index)
{
    
    public DLink Prev = prev;
    public DLink? Next;
    [DebuggerBrowsable(DebuggerBrowsableState.Never)]
    public long Value = value;
    [DebuggerBrowsable(DebuggerBrowsableState.Never)]
    public int Index = index;
}
[DebuggerDisplay("MyPrio({Sum}, {Index})")]
public struct MyPrio(long sum, int index) : IComparable<MyPrio>
{
    public long Sum = sum;
    public int Index = index;

    public int CompareTo(MyPrio other)
    {
        if (Sum != other.Sum)
        {
            return Sum > other.Sum ? 1 : -1;
        }
        return Index - other.Index;
    }
}