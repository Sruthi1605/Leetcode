class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.split()
        banned_set = set(banned)
        count = {}
        for word in words:
            if word not in banned_set:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] += 1
        most_common = ""
        max_count = 0
        for word in count:
            if count[word] > max_count:
                max_count = count[word]
                most_common = word
        return most_common