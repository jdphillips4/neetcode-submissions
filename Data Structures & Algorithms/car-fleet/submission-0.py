class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force:
        # loop through for each hour and add the speed ot the position of each car
        # have a conditional if any fleets are formed
        # count fleets at the end

        # more optimal: probably stack becaue thats the section
        # if car ahead is faster, will never catch it
        # not sure how to think about what to put into the stack, what order
        # the key was to think about times to reach target
        #Hints:
        # sort based on positions descending order
        # use time = (target - position) / speed
        # form fleet if car ahead has >=time as car behind
        # then to keep track of # fleets use stack
        # iterate sorted array, compute time, if curr car tim <= top stack itjoins same fleet
        # else forms new fleet, push new time onto stack, length of stack at end represents total fleets


        #how to sort one array and then others in the same way
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            time = (target - p) / s #decimal division // is integer
            if not stack or time > stack[-1] : #new fleet, <= means it catches
                stack.append(time)
        return len(stack)

