class Solution(object):
    def minimumHealth(self, damage, armor):
        return sum(damage)-armor+1 if max(damage)>armor else sum(damage)-max(damage)+1    
            