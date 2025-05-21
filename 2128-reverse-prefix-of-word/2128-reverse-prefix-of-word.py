class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        res=""

        ind=word.find(ch)
        if ind == "-1":
            return word
        rev=word[:ind+1][::-1]
        secword=word[ind+1:]

        return rev+secword

        

