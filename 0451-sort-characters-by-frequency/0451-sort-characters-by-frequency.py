class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for x in s:
            freq[x] += 1 
        res = ""
        freq_lst = freq.items()
        freq_lst.sort(key = lambda x: -x[1])
        for x in freq_lst:
            res += x[0] * x[1]
        return res
        
        
        