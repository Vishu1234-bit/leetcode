import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        self.follows[userId].add(userId)
    def getNewsFeed(self, userId: int) -> List[int]:
        if(userId not in self.follows):
            return []
        heap=[]
        for users in self.follows[userId]:
            for tweets in self.tweets[users][-10:]:
                heapq.heappush(heap,tweets)
                if(len(heap)>10):
                    heapq.heappop(heap)
        return [tweetId for _,tweetId in sorted(heap,reverse=True)]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId!=followerId and followeeId in self.follows[followerId]):
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
