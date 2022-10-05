class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        
        users = defaultdict(list)
        
        # scan all the tuples (username, timestamp, website) sorted by username and by timestamp
        # for each user append to the list of websites he visited, the websited are already in chronologically order
        for (user, time, site) in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            users[user].append(site)
        
        # at this point we have a dictionary with usernames as keys an list of visited websites by the user as value
        # username : sorted_list_of_visited_websited
        
        # now i create a dictionary with a specific pattern(tuble of 3 websites) as key and the number of users the
        # visited that three websites as value (the score)
        # pattern : score
        patterns = defaultdict(int)
        for user, sites in users.items():
            # here i use set() to the combinations to eliminate the duplicates
            # if a user visits a website four times i will count that pattern two times
            # but i need to count it just one time
            for combination in set(combinations(sites, 3)):
                patterns[combination] += 1
        
        # sort the pattern in lexicographically order and
        # return the pattern with the max value
        return max(sorted(patterns), key=patterns.get)