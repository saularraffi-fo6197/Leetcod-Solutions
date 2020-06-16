class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        s_rev = s[::-1]

        int_val = 0

        prev = ''

        for rom_val in s_rev:
            if rom_val == 'I':
                if prev == 'V' or prev == 'X':
                    int_val = int_val - 1
                else:
                    int_val = int_val + 1

            elif rom_val == 'V':
                int_val = int_val + 5

            elif rom_val == 'X':
                if prev == 'L' or prev == 'C':
                    int_val = int_val - 10
                else:
                    int_val = int_val + 10

            elif rom_val == 'L':
                int_val = int_val + 50

            elif rom_val == 'C':
                if prev == 'D' or prev == 'M':
                    int_val = int_val - 100
                else:
                    int_val = int_val + 100

            elif rom_val == 'D':
                int_val = int_val + 500
                
            elif rom_val == 'M':
                int_val = int_val + 1000

            prev = rom_val

        return int_val