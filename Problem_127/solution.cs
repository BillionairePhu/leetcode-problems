public partial class Solution {
    [TestMethod]
    public void LadderLengthTest()
    {
        Console.WriteLine(LadderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
        Console.WriteLine(LadderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));
    }
    public int LadderLength(string beginWord, string endWord, IList<string> wordList)
    {
        int numsChain = 1;
        List<string> currentLink = [beginWord];
        List<string> nextLink = [];
        while (currentLink.Count > 0 && wordList.Count > 0)
        {
            numsChain++;
            for (int i = 0; i < wordList.Count; i++)
            {
                string wordInWordList = wordList[i];
                foreach (var word in currentLink)
                {
                    if (NotCloseEnough(wordInWordList, word))
                    {
                        continue;
                    }
                    if (wordInWordList == endWord)
                    {
                        return numsChain;
                    }
                    else
                    {
                        nextLink.Add(wordInWordList);
                        wordList.RemoveAt(i);
                        i--;
                        break;
                    }
                }
            }
            currentLink.Clear();
            (currentLink, nextLink) = (nextLink, currentLink);
        }
        return 0;
    }
    public bool NotCloseEnough(string a, string b)
    {
        int diffcount = 0;
        for (int i = 0; i < a.Length; i++)
        {
            if (a[i] != b[i]) diffcount += 1;
        }
        return diffcount > 1;
    }
}