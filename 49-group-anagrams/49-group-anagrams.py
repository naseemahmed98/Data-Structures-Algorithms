class Solution(object):
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)
        
        for x in strs:
            count = [0] * 26 
            for y in x:
                count[ord(y)-ord('a')] +=1 
            res[tuple(count)].append(x)
        
        return res.values()
                