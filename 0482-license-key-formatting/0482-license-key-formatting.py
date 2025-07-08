class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()        
        
        s = s[::-1]     
        
        groups = [s[i:i+k] for i in range(0, len(s), k)]        
        
        return '-'.join(groups)[::-1]
        