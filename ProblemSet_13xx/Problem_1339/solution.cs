using System.Xml;

Solution s = new();
TreeNode t = new TreeNode(1,
    new TreeNode(2,
        new TreeNode(4),
        new TreeNode(5)
    ),
    new TreeNode(3,
        new TreeNode(6)
    )
);
Console.WriteLine(s.MaxProduct(t));

t = new TreeNode(1,
    new TreeNode(2,
        new TreeNode(3),
        new TreeNode(4,
            new TreeNode(5),
            new TreeNode(6)
        )
    )
);
Console.WriteLine(s.MaxProduct(t));


public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class Solution {
    public int sum;
    public long max;
    public int MaxProduct(TreeNode root)
    {
        max = 0;
        sum = SumTree(root);
        SumWithProd(root);
        return (int)(max % 1000000007);
    }
    public int SumTree(TreeNode root)
    {
        if (root == null) return 0;
        return root.val + SumTree(root.left) + SumTree(root.right);
    }
    public long SumWithProd(TreeNode root)
    {
        if (root == null) return 0;
        long left = SumWithProd(root.left);
        long right = SumWithProd(root.right);

        max = Math.Max(max, left * (sum - left));
        max = Math.Max(max, right * (sum - right));
        return root.val + left + right;
    }
}