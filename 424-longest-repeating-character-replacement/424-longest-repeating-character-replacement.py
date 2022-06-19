class Solution:
    def characterReplacement(self, s,k):
        windowStart = 0
        maxRepeatLetterCount = 0
        maxLength = 0
        
        char_freq = {}
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar not in char_freq:
                char_freq[rightChar] = 0
            char_freq[rightChar] += 1
            
            maxRepeatLetterCount = max(maxRepeatLetterCount, char_freq[rightChar])
            
            if (windowEnd-windowStart+1 - maxRepeatLetterCount) > k:
                leftChar = s[windowStart]
                char_freq[leftChar] -= 1
                windowStart += 1
            
            
            maxLength = max(maxLength, windowEnd-windowStart+1)
        return maxLength