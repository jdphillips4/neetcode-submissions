class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for s in strs:
            appended = False
            if not len(output)==0:
                for j in output:
                    if sorted(s) == sorted(j[0]):
                        j.append(s)
                        appended = True
                        break
            if not appended:
                output.append([s])
        
        return output
        