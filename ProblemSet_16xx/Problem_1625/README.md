# 🔥 Leetcode Problem (1625)

> **Problem:** [Lexicographically Smallest String After Applying Operations](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/)<br />
> **Difficulty:** Medium<br/>
> **Tags:** `String`, `Depth-First Search`, `Breadth-First Search`, `Enumeration`

---

### ✅ Intuition

This is a very interesting problem that requires mathematical knowledge. In my case, I just do the brute-force methods but it works because the total number of possible values is capped at `n * d^2`. How convenient!

To understand why, I think the editorial did this very well. => I'm copying down here.

The problem involves two operations:

Accumulate: Add the odd-numbered elements of ( s ) by ( a ). If the sum exceeds ( 9 ), wrap around to ( 0 ) and continue adding.
Rotate: Rotate ( s ) to the right by ( b ) bits.
These operations can be performed an unlimited number of times, and the question asks for the lexicographically smallest string that can be obtained.

Noting that the length of ( s ) is even, if ( b ) is even, then regardless of how many rotations are performed, we can only apply the accumulation operation to the odd-numbered elements of ( s ). However, if ( b ) is odd, both the odd- and even-numbered elements of ( s ) can be modified through accumulation, each potentially a different number of times.

From the above observation, we see that the number of cumulative operations and the number of rotations are independent of each other. The number of rotations does not affect whether even positions can be accumulated. Therefore, we can first enumerate the number of rotations and then enumerate the number of cumulative operations to find the lexicographically smallest result.

More specifically, we proceed as follows:

Enumerate the number of rotations, letting ( t ) denote the string after rotating ( s ). Since rotation eventually cycles, and there are at most ( n ) unique rotations (where ( n ) is the length of ( s )), we use an array vis to record whether a position has already been visited. Once a previously visited position is encountered, the enumeration stops.
For each ( t ), enumerate the number of times ( j ) the odd digits of ( t ) are incremented, and then the number of times ( k ) the even digits are incremented. Since each element’s value lies in ([0, 9]), performing more than 9 additions would necessarily repeat a previous state. Specifically, if ( b ) is even, ( k )’s upper limit is ( 0 ); otherwise, it is ( 9 ).

---

### 🧪 Complexity

Let `n` be the length of `s`, and `d` be the upper limit on the number of cumulative sums, which is 10 in this problem.

- **Time:** O(n^2 d^2) => remember that there is the cost of string comparison, which is O(n)
- **Space:** O(n d^2) => Since I'm storing all possible value in a set, the complexity scales with the value count