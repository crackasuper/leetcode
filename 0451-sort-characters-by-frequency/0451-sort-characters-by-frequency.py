class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        buckets = [[] for _ in range(len(s) + 1)]

        for c, freq in collections.Counter(s).items():
            buckets[freq].append(c)

        for freq in reversed(range(len(buckets))):
             for c in buckets[freq]:
                 ans.append(c * freq)

        return ''.join(ans)
            