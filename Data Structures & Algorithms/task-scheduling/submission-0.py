class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        # O(n*m)
        count = Counter(tasks) #creates hashmap of the count of each element
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # pairs of values of [-cnt, idleTime]

        while maxHeap or queue: #as long as one is not empty we have tasks to process
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # pops and decrements count in one go
                if cnt:
                    queue.append([cnt, time + n]) # add cnt and next available time to queue
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time

