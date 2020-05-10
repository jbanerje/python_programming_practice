''' Reverse of a digit : eg : 105 should return 501; -105 should return -501'''
def reverse_digit(num):
    rev_num = 0 ; abs_num = abs(num)

    while abs_num > 0 :
        rev_num = (10 * rev_num +  abs_num % 10)
        abs_num //= 10
    return -rev_num if num < 0 else rev_num

if __name__ == '__main__':
    num=-105
    print('Reverse of {}  is {}'. format(num,  reverse_digit(num)))
