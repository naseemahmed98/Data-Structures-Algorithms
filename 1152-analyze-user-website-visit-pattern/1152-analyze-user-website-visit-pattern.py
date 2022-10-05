class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        
        users = defaultdict(list)
     
        

        for (user, time, site) in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            
            users[user].append(site)
        
        
        patterns = defaultdict(int)
        for user, sites in users.items():
            print(user,'hi')
            for combination in set(combinations(sites, 3)):
                print(combination)
                patterns[combination] += 1
        patternItems = list(patterns.items())
        
        patternItems.sort(key = lambda x:(-x[1],x[0]))
      
        return patternItems[0][0]