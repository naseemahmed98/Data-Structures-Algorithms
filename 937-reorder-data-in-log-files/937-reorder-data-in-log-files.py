class Solution:
    #T=O(m*nlgn),S=O(mn)
    #m=len(log),n=number of logs
    def reorderLogFiles(self, logs):
        letter = []
        digit = []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        
		#sort by content and if there is a tie, sort by id: sort by id first and then sort by content as sort is a stable algo
        letter.sort(key = lambda x: x.split()[0]) #sort by identifier if there is a tie with suffix
        letter.sort(key = lambda x: x.split()[1:])
        
        return letter + digit