class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for num in range(left,right+1):
            n=num
            isval=True

            while n>0:
                dig=n%10
                if dig==0 or num%dig!=0:
                    isval=False
                    break
                n=n//10
            
            if isval is True:
                res.append(num)

        return res