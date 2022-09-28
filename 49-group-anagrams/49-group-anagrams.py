class Solution(object):
    def groupAnagrams(self, strs):
        dct = collections.defaultdict(list)
        for x in strs:
            sorted_word = "".join(sorted(x))
            
            dct[sorted_word].append(x)
          
        return dct.values()