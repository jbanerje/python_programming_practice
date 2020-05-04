'''Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321
'''
class Reverse(object):
    rev_num = 0
    neg_num = False

    def __init__(self, num):
        self.num = num

    def reverse_an_int(self):
        if self.num == 0:
            return self.num
        
        elif self.num < 0:
            self.num  = self.num * -1
            self.neg_num = True

        while self.num > 0:
            quo = self.num % 10
            self.rev_num = (self.rev_num * 10) + quo
            self.num = int(self.num/10)
        
        if self.neg_num == True:
            return self.rev_num * -1
        else:
            return self.rev_num

if __name__ =="__main__":
    rev_num = Reverse(25)
    result =  rev_num.reverse_an_int()
    print(result)

