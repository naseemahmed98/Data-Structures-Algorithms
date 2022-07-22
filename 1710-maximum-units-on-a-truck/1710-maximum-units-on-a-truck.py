class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: -x[1])
        unitCounter = 0
        for x, y in boxTypes:
            #if truckSize == 0:
             #   return unitCounter
            if truckSize >= x:
                unitCounter += x * y
                truckSize -= x
            elif truckSize < x:
                unitCounter += (truckSize) * y
                truckSize = 0 
        return unitCounter
        
        
        
            
        