class Solution(object):
    def minimumHealth(self, damage, armor):
        totalHealth = 1
        maxDamage = float("-inf")
        for x in damage:
            if x > maxDamage:
                maxDamage = x 
        
        armorAccess = True 
        for x in damage:
            if x == maxDamage and armorAccess:
                if x > armor:
                    totalHealth += (x-armor)
                armorAccess = False 
                continue 
            totalHealth += x 
        
        return totalHealth
                
            