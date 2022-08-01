class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        banned_set = set(banned)
        for x in "!?',;.":
            paragraph = paragraph.replace(x," ")
        
        word_freq={}
        max_word = ""
        counter = 0
        
        for x in paragraph.split():
            if x not in banned_set:
                if x not in word_freq:
                    word_freq[x] = 1 
                else:
                    word_freq[x] += 1
                    
                if word_freq[x] > counter:
                    counter = word_freq[x]
                    max_word = x
        
   
        return max_word
