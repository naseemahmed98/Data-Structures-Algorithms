class Solution(object):
    def groupAnagrams(self, strs):
        dct = collections.defaultdict(list)
        for x in strs:
            sortedWord = ''.join(sorted(x))
            dct[sortedWord].append(x)
        return dct.values()
      