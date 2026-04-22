class Solution:

    def encode(self, strs: List[str]) -> str:
        #naive use delimiter, will break if spaces 
        #better us length of string in delimiter 4,string
        result = ""
        for s in strs:
            result = result + str(len(s)) + "," + s 
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s): 
            j=i
            while s[j] != ",":
                j += 1
            # j now points do delimiter index
            # string from i to j is number representing length
            length = int(s[i:j]) #doesnt include last index 
            result.append(s[j + 1:j + length + 1]) # need +1 because of last index not being included
            i = j + length + 1 # i is at the start of the next number

        return result
