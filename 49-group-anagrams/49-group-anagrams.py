class Solution(object):
    def groupAnagrams(self, strs):
        dct = {}
        for x in strs:
            sorted_word = "".join(sorted(x))
            if sorted_word in dct:
                dct[sorted_word].append(x)
            else:
                dct[sorted_word] = [x] 
        return dct.values()