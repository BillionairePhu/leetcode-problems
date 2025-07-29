using System.Collections;
using System.Diagnostics.CodeAnalysis;
using System.Reflection;
using Microsoft.VisualStudio.TestPlatform.Utilities;

namespace LeetCode.CollectionComparer;

public struct ParameterResultPair<TParameter, TResult>
{
    public ParameterResultPair(TParameter parameter, TResult result)
    {
        Parameter = parameter;
        Result = result;
    }
    public TParameter Parameter;
    public TResult Result;
}

public class EnumerableItemComparer<T> : IEqualityComparer<IEnumerable<T>>
{
    public IEqualityComparer<T> ItemEqualityComparer;
    public EnumerableItemComparer(IEqualityComparer<T>? itemEqualityComparer = null)
    {
        if (itemEqualityComparer == null) ItemEqualityComparer = EqualityComparer<T>.Default;
        else ItemEqualityComparer = itemEqualityComparer;
    }
    public bool Equals(IEnumerable<T>? x, IEnumerable<T>? y)
    {
        if (x == y) return true;
        else if (x == null || y == null) return false;
        var xnumerator = x.GetEnumerator();
        var ynumerator = y.GetEnumerator();
        while (xnumerator.MoveNext())
        {
            if (!(ynumerator.MoveNext() && ItemEqualityComparer.Equals(xnumerator.Current, ynumerator.Current)))
            {
                return false;
            }
        }
        return true;
    }

    public int GetHashCode([DisallowNull] IEnumerable<T> obj)
    {
        var a = obj.First();
        return a == null ? int.MinValue : a.GetHashCode();
    }
}

public class DictionaryItemComparer<TKey, TValue> : IEqualityComparer<Dictionary<TKey, TValue>> where TKey : notnull
{
    public IEqualityComparer<TValue> ItemEqualityComparer;
    public DictionaryItemComparer(IEqualityComparer<TValue>? itemEqualityComparer = null)
    {
        if (itemEqualityComparer == null) ItemEqualityComparer = EqualityComparer<TValue>.Default;
        else ItemEqualityComparer = itemEqualityComparer;
    }
    public bool Equals(Dictionary<TKey, TValue>? x, Dictionary<TKey, TValue>? y)
    {
        if (x == y) return true;
        else if (x == null || y == null) return false;
        else if (x.Count != y.Count) return false;
        foreach (var item in x)
        {
            if (!(y.TryGetValue(item.Key, out TValue? value) && ItemEqualityComparer.Equals(item.Value, value)))
            {
                return false;
            }
        }
        return true;
    }

    public int GetHashCode([DisallowNull] Dictionary<TKey, TValue> obj)
    {
        int totalhashcode = 0;
        foreach (var item in obj)
        {
            totalhashcode += item.Key.GetHashCode() ^ ((item.Value == null) ? 21062007 : item.Value.GetHashCode());
        }
        return totalhashcode;
    }
}

public class HashSetItemComparer<T> : IEqualityComparer<HashSet<T>>
{
    public bool Equals(HashSet<T>? x, HashSet<T>? y)
    {
        if (x == y) return true;
        else if (x == null || y == null) return false;
        else if (x.Count != y.Count) return false;
        foreach (var item in x)
        {
            if (!y.TryGetValue(item, out _))
            {
                return false;
            }
        }
        return true;
    }

    public int GetHashCode([DisallowNull] HashSet<T> obj)
    {
        int totalhashcode = 0;
        foreach (var item in obj)
        {
            totalhashcode += (item == null) ? 22102003 : item.GetHashCode();
        }
        return totalhashcode;
    }
}