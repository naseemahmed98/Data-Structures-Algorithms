class Solution(object):
    def minimumHealth(self, damage, armor):
        total_health = 1
        damage.sort(reverse = True)
        armor_state = True 
        
        for x in damage:
            if armor_state:
                if x >= armor:
                    total_health += (x - armor)
                armor_state = False
                continue
            
            total_health += x
            
        return total_health
                
            