"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # looking for any overlap
        # if min of ends is > max of starts theres overlap
        # brute force: n^2
        # for i in range(len(intervals)):
        #     A = intervals[i]
        #     for j in range(i + 1, len(intervals)):
        #         B = intervals[j]
        #         if (min(A.end, B.end) > max(A.start, B.start)):
        #             return False
        # return True

        # optimal nlogn sort by start then just compare end and start of consecutive
        intervals.sort(key = lambda i: i.start) # sort i by start time
        n = len(intervals)
        for i in range(n-1):# n-1 so i+1 works
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
