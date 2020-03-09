#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.l = []
        self.m = dict()

    def get(self, key: int) -> int:
        if(key in self.m):
            self.l.remove([key, self.m[key]])
            self.l.append([key, self.m[key]])
            return self.m[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.m):
            self.l.remove([key, self.m[key]])
            self.l.append([key, value])
            self.m[key] = value
        else:
            self.l.append([key, value])
            self.m[key] = value
            if(len(self.l) > self.cap):
                del self.m[self.l[0][0]]
                self.l.pop(0)

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
param_1 = cache.get(0)
cache.put(1, 1)
print(cache.l, cache.m)
cache.put(2, 2)
print(cache.l, cache.m)
cache.get(1)
print(cache.l, cache.m)
cache.put(3, 3)
print(cache.l, cache.m)
cache.get(2)
cache.put(4, 4)
cache.get(1)    
cache.get(3)     
print(cache.l)
# @lc code=end

