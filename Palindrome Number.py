class Solution:

    def isPalindrome(self, x):
        if x != abs(x):
            return False

        l_index = 0
        r_index = len(str(x)) - 1

        while l_index <= r_index:
            l_val = int(x / 10 ** l_index % 10)
            r_val = int(x / 10 ** r_index % 10)

            print (str(l_val), ' =? ', str(r_val))

            if l_val != r_val:
                return False

            l_index = l_index + 1
            r_index = r_index - 1

        return True

sol = Solution()
print(sol.isPalindrome(1234321))