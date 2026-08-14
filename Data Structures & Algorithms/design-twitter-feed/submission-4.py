class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = {} # Stores user_id -> {user_id}
        self.tweet_map = {} # Stores user_id -> [(count, tweet_id)]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet_map:
            self.tweet_map[userId].append((self.count, tweetId))
        
        else:
            self.tweet_map[userId] = [(self.count, tweetId)]
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []

        if userId in self.follow_map:
            self.follow_map[userId].add(userId)
        else:
            self.follow_map[userId] = {userId}
        
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                idx = len(self.tweet_map[followee_id]) - 1
                count, tweet_id = self.tweet_map[followee_id][idx]
                heapq.heappush(max_heap, [count, tweet_id, followee_id, idx - 1])

        while max_heap and len(result) < 10:
            count, tweet_id, followee_id, idx = heapq.heappop(max_heap)
            result.append(tweet_id)
            if idx >= 0:
                count, tweet_id = self.tweet_map[followee_id][idx]
                heapq.heappush(max_heap, [count, tweet_id, followee_id, idx - 1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            self.follow_map[followerId] = {followeeId}    


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
        
