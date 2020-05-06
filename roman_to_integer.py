''' Roman to Integer  (https://leetcode.com/problems/roman-to-integer/) '''

class Solution(object):
    
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    cri_letters=['V', 'X', 'L', 'C', 'D', 'M']
    sol_int = 0
    hold_value = False
    def __init__(self, s):
        self.s = s
    
    def romanToInt(self):
        """
        :type s: str
        :rtype: int
        """
        for pos, roman_letter in enumerate(self.s):
            print('Roman Letter-->', pos, roman_letter)
            if pos>0 and roman_letter in self.cri_letters and self.s[pos-1] == 'I':
               self.sol_int = self.sol_int -2 + self.roman_dict[roman_letter]
               print('At 1', self.sol_int)
            else:
              self.sol_int += self.roman_dict[roman_letter]  
              print('At 2', self.sol_int)

        print(self.sol_int)

roman_to_int = Solution('XC')
roman_to_int.romanToInt()
