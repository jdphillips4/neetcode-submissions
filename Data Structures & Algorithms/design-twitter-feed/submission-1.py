class Twitter:

    def __init__(self):
        # hashmap user to set of followees
        # userId to list of [count, tweetIDS]
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # hashmap user to list of tweets
        # need tweetids, and time (total tweets)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement for maxHeap properties

    def getNewsFeed(self, userId: int) -> List[int]:
        # retrieve 10 most recent tweets 
        # most recent, but cant just compare tweetIDs
        # user to followees to times & tweetIDs
        # time is count of tweet, make neg, add from frontier to heap
        res = [] # ordered starting from most recent
        maxHeap = []

        self.followMap[userId].add(userId) # edge case always follow self
        for followeeId in self.followMap[userId]: 
            # add to heap so its sorted by most neg, is most recent
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # could hashmap follower to list followees
        # but unfollow makes removes important, hashset ins/rem O(1)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
