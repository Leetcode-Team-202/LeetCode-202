#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#
from random import randint, sample
# @lc code=start
class Codec:
    def __init__(self):
        self.short_dict = {}
        self.long_dict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.long_dict.keys():
            word = self.generate_word()
            while(word in self.short_dict.keys()):
                word = self.generate_word()
            self.long_dict[longUrl] = word
            self.short_dict[word] = longUrl

        return self.long_dict[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_dict[shortUrl]

    def generate_word(self):
        "generate unique 6 bit code from dic"
        dic = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        word = sample(dic,6)
        return 'http://tinyurl.com/' + str(word)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
Codec().encode("https://leetcode.com/problems/design-tinyurl")
print(Codec().decode("http://tinyurl.com/4e9iAk"))
