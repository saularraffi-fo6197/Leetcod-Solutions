class Solution(object):

    def reverse(self, x):

        neg = False

        if x < 0:
            neg = True
            x = x * -1

        if x == 0 or x > 2 ** 31 - 1:
            return 0

        rev = str(x)[::-1]

        if int(rev) > 2 ** 31 - 1:
            return 0
        elif neg:
            return int(rev) * -1
        else:
            return int(rev)