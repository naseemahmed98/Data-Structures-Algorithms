class Solution(object):
    def platesBetweenCandles(self, s, queries):
        length = len(s)
        prefix_sum = [0] * length
        
        if s[0] == '*':
            prefix_sum[0] = 1    
        
        for i in range(1, length):
            if s[i] == '*':
                prefix_sum[i] = 1 + prefix_sum[i - 1]
            else:
                prefix_sum[i] = prefix_sum[i - 1]
       
                
        leftArray = [-2] * length
        if s[0] == '|':
            leftArray[0] = 0
        
        for i in range(1, length):
            if s[i] == '|':
                leftArray[i] = i
            else:
                leftArray[i] = leftArray[i - 1]
 
        
        rightArray = [float("inf")] * length
        if s[-1] == '|':
            rightArray[-1] = length - 1
        
        for i in range(length - 2, -1, -1):
            if s[i] == '|':
                rightArray[i] = i
            else:
                rightArray[i] = rightArray[i + 1]
     
        
        answers = []
        for start, end in queries:
            leftIndex = rightArray[start]
            rightIndex = leftArray[end]
            if rightIndex - leftIndex > 1:
                num_of_stars = prefix_sum[rightIndex] - prefix_sum[leftIndex]
                answers.append(num_of_stars)
            else:
                answers.append(0)
        
        return answers