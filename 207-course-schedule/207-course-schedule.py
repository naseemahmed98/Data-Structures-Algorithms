class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        num_pre = [0] * numCourses 
        prereq_list = []
        for x in range(numCourses):
            prereq_list.append([])
        no_prereqs = []
        
        for b,a in prerequisites:
            num_pre[b] += 1 
            prereq_list[a].append(b)
        
        for x in range(numCourses):
            if num_pre[x] == 0:
                no_prereqs.append(x)
        
        counter = 0 
        while no_prereqs:
            course = no_prereqs.pop(0)
            counter += 1 
            for x in prereq_list[course]:
                num_pre[x] -= 1 
                if num_pre[x] == 0:
                    no_prereqs.append(x)
                    
        if counter == numCourses:
            return True 
        else:
            return False
    
    
   
