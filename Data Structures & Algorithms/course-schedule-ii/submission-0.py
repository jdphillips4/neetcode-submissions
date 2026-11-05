class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same as before exept not possible reutrn empty array
        # could track order with dfs
        # adjacency list, topological sort
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # course can ves visited, visiting, unvisited
        visitSet = set()
        cycleSet = set()
        output = []

        def dfs(crs):
            if crs in cycleSet:
                # found loop, not possible return []
                return False
            if crs in visitSet:
                return True
            # if preMap[crs] == []:
                # possible to complete this course
            cycleSet.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False: return False
            cycleSet.remove(crs)
            visitSet.add(crs)
            #preMap[crs] = []
            # this course can be reached
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return output