class Solution(object):
    def wordBreak(self, s, wordDict):
        memory = {}
        def makeWord(string):
            if not string:
                return True
            if string in memory:
                return memory[string]
            for word in wordDict:
                ind = string.find(word)
                if ind == 0:
                    res = makeWord(string[len(word):])
                    memory[string[len(word):]] = res
                    if res:
                        return True
            return False
        return makeWord(s)