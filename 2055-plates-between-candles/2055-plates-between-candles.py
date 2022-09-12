class Solution(object):
    def platesBetweenCandles(self, s, queries):
     
		p = [i for i in range(len(s)) if s[i] == '|']
    

		res = []
		for f,t in queries: 
			l = bisect.bisect_left(p, f)
			r = bisect.bisect_right(p, t)
			res.append(p[r-1] - p[l] - (r-1-l) if r > l else 0)

		return res