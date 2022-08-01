class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        
        paragraph = paragraph.lower()
        for x in "!?',;.'":
            paragraph = paragraph.replace(x," ")
            
        word_freq = {}
        counter = 0 
        max_word = ""
        
        
        for x in paragraph.split():
            if x not in banned:
                if x not in word_freq:
                    word_freq[x] = 1 
                else:
                    word_freq[x] += 1 
                if word_freq[x] > counter:
                    counter = word_freq[x]
                    max_word = x
        return max_word
        