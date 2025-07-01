class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []

        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    time_str = "{}:{:02d}".format(hour, minute)
                    result.append(time_str)

        return result