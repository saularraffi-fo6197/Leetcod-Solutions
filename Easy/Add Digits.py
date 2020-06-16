class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sum = 0

        while int(num / 10) != 0:
            while num != 0:
                sum = sum + int(num % 10)
                num = int(num / 10)
            num = sum
            sum = 0

        return num