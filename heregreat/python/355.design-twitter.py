#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from queue import Queue

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = {}
        self.friends = {}
        self.timetweetId = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.tweets.keys():
            self.tweets[userId] = []
        self.tweets[userId].append(self.time)
        self.timetweetId[self.time] = tweetId
        self.time += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tem = []
        res = []
        if (userId not in self.friends.keys()):
            self.friends[userId] = set()
        self.friends[userId].add(userId)
        for ppl in self.friends[userId]:
            if ppl in self.tweets.keys():
                for i in self.tweets[ppl]:
                    tem.append(i)
        
        tem = sorted(tem, reverse = True)
        tem = tem[0:10]
        for i in tem:
            res.append(self.timetweetId[i])
        return res

                    

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if (followerId not in self.friends.keys()):
            self.friends[followerId] = set()
        self.friends[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if(followerId != followeeId):
            if followerId in self.friends.keys():
                self.friends[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

