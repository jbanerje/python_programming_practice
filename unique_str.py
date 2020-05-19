# Implement an algorithm to determine if a string has all unique character not using  additional data structure
import time

def chk_str(my_str):
    ''' Using a list data structure '''
    
    unique_flg = True
    str_sorted = sorted(my_str)
    print(str_sorted)
    for pos in range(len(str_sorted)):
        if pos==0:
            hold_letter = str_sorted[pos]
        else:
            if str_sorted[pos] == hold_letter:
                unique_flg = False
                break
            else:
                hold_letter = str_sorted[pos]    
    return unique_flg

def chk_str_brute_force(my_str):
    ''' Using a list data structure '''
    str_list = [] ; unique_flg = True
    
    for letter in my_str:
        if letter in str_list:
            unique_flg = False
            break
        else:
            str_list.append(letter)
    
    return unique_flg

if __name__ == '__main__':
    # print(chk_str_brute_force('acbde'))
    print(chk_str('acbde'))
    print(time.process_time_ns())
