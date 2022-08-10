class Solution(object):
    def topKFrequent(self, words, k):
        freq ={}
        res = []
        for x in words:
            if x in freq:
                freq[x] += 1 
            else:
                freq[x] = 1
        
        freq_lst = list(freq.items())
        freq_lst.sort(key = lambda x: (-x[1],x[0]))
        for x in range(k):
            res.append(freq_lst[x][0])
        return res


