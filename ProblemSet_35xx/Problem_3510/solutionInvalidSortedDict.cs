// this Solution is ~3.5x slower, but slightly more readable

public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        if (nums.Length < 2) return 0;
        // if (nums[0] == 1000000000 && nums[1] == 999999999) return 99998;
        
        int op = 0;
        SortedDictionary<MyPrio, DLink> pq = new();
        int decrease = 0;
        DLink nilroot = new DLink(null, int.MinValue, -1);
        DLink last = nilroot;
        for (int i = 0; i < nums.Length - 1; i++)
        {
            last.Next = new DLink(last, nums[i], i);
            last = last.Next;
            pq.Add(new MyPrio(nums[i] + nums[i + 1], i), last);
            if (nums[i] > nums[i + 1]) decrease++;
        }
        last.Next = new DLink(last, nums[nums.Length - 1], nums.Length - 1);
        last = last.Next;
        nilroot.Next.Prev = null;

        while (decrease > 0)
        {
            op += 1;
            MyPrio prio = pq.Keys.First();
            DLink link = pq[prio];

            DLink linkplus1 = link.Next;
            // Debug.Assert(linkplus1 != null);
            if (link.Value > linkplus1.Value) decrease--;
            DLink? linkplus2 = linkplus1.Next;
            pq.Remove(new MyPrio(linkplus1.Value + link.Value, link.Index));
            if (linkplus2 != null)
            {
                if (linkplus1.Value > linkplus2.Value) decrease--;
                pq.Remove(new MyPrio(linkplus1.Value + linkplus2.Value, linkplus1.Index));
                linkplus2.Prev = link;
                if (prio.Sum > linkplus2.Value) decrease++;
                pq.Add(new MyPrio(prio.Sum + linkplus2.Value, link.Index), link);
            }
            link.Next = linkplus2;

            DLink? linkminus1 = link.Prev;
            if (linkminus1 != null)
            {
                if (linkminus1.Value > link.Value) decrease--;

                if (linkminus1.Value > prio.Sum) decrease++;
                pq.Remove(new MyPrio(linkminus1.Value + link.Value, linkminus1.Index));
                pq.Add(new MyPrio(linkminus1.Value + prio.Sum, linkminus1.Index), linkminus1);
            }

            link.Value = prio.Sum;
        }

        return op;
    }
}

// [DebuggerDisplay("DLink({Value}, {Index})")]
public class DLink(DLink prev, long value, int index)
{
    
    public DLink Prev = prev;
    public DLink? Next;
    // [DebuggerBrowsable(DebuggerBrowsableState.Never)]
    public long Value = value;
    // [DebuggerBrowsable(DebuggerBrowsableState.Never)]
    public int Index = index;
}
// [DebuggerDisplay("MyPrio({Sum}, {Index})")]
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