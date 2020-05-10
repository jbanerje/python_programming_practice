''' Check of a decimal interger is a palindrome '''

def reverse_digit(num):
    rev_num = 0 ; abs_num = abs(num)

    while abs_num > 0 :
        rev_num = (10 * rev_num +  abs_num % 10)
        abs_num //= 10
    return -rev_num if num < 0 else rev_num

if __name__ == '__main__':
    num = 121
    if reverse_digit(num) == num :
       print('Palindrome') 
    else:
       print('Not a palindrome')
