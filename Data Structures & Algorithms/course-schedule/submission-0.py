class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # only pairs?
        # loops make impossible
        # numCourses, then all prereq pairs
        # can get thru numCourses?
        #[a,b] = take b before a

        #can you have many courses and empty prereqs?

        # i think were just looking for loops that would make it impossible

        # [a,b] start at b, see if b is reachable looking for a as pre for something else then that thing... until b is found again or not

        # dfs from each point see if its reachable again
        # ^ brute force probably better way
        # loop actually doesnt matter if there is a way into it

        # hashmap course, prereqs [], 
        # dfs from 0 to n-1, run dfs on neighbors
        # pop of pres from [] until all are empty lists []
        # O(n+ p) visit every node and move along every edge
        # visited set detect loops

        preMap = {i:[] for i in range(numCourses)} # empty set for each
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #visitSet = all courses along current DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet: # found loop
                return False
            if preMap[crs] == []: # no pres, crs can be completed
                return True
            visitSet.add(crs)
            for pre in preMap[crs]: # loop found immediately return F
                if not dfs(pre): return False
            visitSet.remove(crs) #went through all dfs, back to here
            preMap[crs] = [] # prevents repeated work
            return True # is possible to complete this crs
        
        for crs in range(numCourses): # could not be fully connected
            if not dfs(crs): return False
        return True

# initialize preMap, declare visitSet
# dfs on crs, check base cases add to set recurse on pres remove form set return true
# loop thorugh all courses running dfs if false return false 
