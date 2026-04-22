class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers stay the same or increase
        left = 0
        right = len(numbers) - 1
        while (True):#doesnt matter if always solution
            if ((numbers[left] + numbers[right]) < target):
                left +=1
            elif ((numbers[left] + numbers[right]) > target):
                right -=1
            else:
                return [left+1,right+1]
        #Brute Force:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if (numbers[i] + numbers[j] == target):
        #             return [i+1,j+1]