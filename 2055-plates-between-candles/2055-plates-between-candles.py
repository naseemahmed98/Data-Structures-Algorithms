class Solution(object):
    def platesBetweenCandles(self, s, queries):

        cand_idx = []
        for idx in range(len(s)):
            if s[idx] == "|":
                cand_idx.append(idx)
        ans = []
        for query in queries:
            left, right = query
            l = bisect.bisect_left(cand_idx, left)
            r = bisect.bisect(cand_idx, right)
            if l == r:
                ans.append(0)
                continue

            l_idx = cand_idx[l]
            
            r_idx = cand_idx[r-1]
            cand_count = r - l

            ans.append(r_idx - l_idx + 1 - cand_count)
            
        return ans