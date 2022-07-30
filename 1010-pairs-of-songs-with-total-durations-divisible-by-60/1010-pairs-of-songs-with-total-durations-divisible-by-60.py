class Solution(object):
    def numPairsDivisibleBy60(self, time):
        remainder_map = {}
        num_pairs = 0 
        for x in time:
            remainder_val = x % 60 
            if remainder_val == 0 and remainder_val in remainder_map:
                num_pairs += remainder_map[remainder_val]
            if (60-remainder_val) in remainder_map:
                num_pairs += remainder_map[60-remainder_val] 
                
       
            if remainder_val not in remainder_map:
                remainder_map[remainder_val] = 1 
            else:
                remainder_map[remainder_val] += 1
                
            
        print(remainder_map)
        return num_pairs
     
      
        