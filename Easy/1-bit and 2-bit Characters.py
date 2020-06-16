class Solution(object):

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        i = 0
        while i < len(bits):
            if i == len(bits) - 1 and bits[i] == 0:
                return True
            elif bits[i] == 1:
                i = i + 2
            else:
                i = i + 1

        return False