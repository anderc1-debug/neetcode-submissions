class Solution:
    def encode(self, strs):
        result = ""
        for word in strs:
            length = len(word)
            result += str(length) + "#" + word
        return result

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res