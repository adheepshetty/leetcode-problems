import unittest
import string, random
class Codec:
    '''
    TinyURL is a URL shortening service where you enter a URL such 
    as https://leetcode.com/problems/design-tinyurl and it returns a short URL 
    such as http://tinyurl.com/4e9iAk.

    Design the encode and decode methods for the TinyURL service. 
    There is no restriction on how your encode/decode algorithm should work. 
    You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can 
    be decoded to the original URL.
    '''
    def __init__(self):
        self.long_to_short = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        
        def generate_shortUrl():
            all_chars = string.ascii_letters + string.digits
            shortUrl = ''.join([random.choice(all_chars) for x in range(6)])
            return shortUrl
    
        
        shortUrl = generate_shortUrl()
        while shortUrl in self.long_to_short.values():
            shortUrl = generate_shortUrl()
            
        self.long_to_short[longUrl] = shortUrl
        
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        for k, v in self.long_to_short.items():
            if v == shortUrl:
                return k
        
        return None

# Your Codec object will be instantiated and called as such:
class Test(unittest.TestCase):
    def test_levelOrder(self):
        url = "https://leetcode.com/problems/design-tinyurl"
        codec = Codec()
        self.assertEqual(codec.decode(codec.encode(url)),url)

   

if __name__ == "__main__":
    print(Codec.__doc__)
    unittest.main()