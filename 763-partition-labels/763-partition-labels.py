class Solution(object):
    def partitionLabels(self, s):
        letter_freq = {}
        partition_freq = {}
        unique_letters = set()
        
        l, r = 0, 0  
        res = []
        for x in s:
            if x not in letter_freq:
                letter_freq[x] = 1 
            else:
                letter_freq[x] += 1 
        print(letter_freq)
        unique_letters.add(s[r])
        print(unique_letters)
        while r < len(s):
         #   print(unique_letters)
            
            if s[r] not in partition_freq:
                partition_freq[s[r]] = 1
                #if letter_freq[s[r]] != 1:
                unique_letters.add(s[r])
            else:
                partition_freq[s[r]] += 1 
            if partition_freq[s[r]] == letter_freq[s[r]]:
                    unique_letters.remove(s[r])
            if not unique_letters:
                res.append(r-l+1)
                l = r+1
          #  print(unique_letters)
            r += 1
        #print('this',partition_freq)
      
        return res            
            
        