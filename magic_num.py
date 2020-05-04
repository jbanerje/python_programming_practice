# Magic Number
def square_of_square(num):
    sum_of_sqr=0
    while num!=0:
        sum_of_sqr += (num%10)*(num%10)
        num = int(num/10)
    return sum_of_sqr


def perform_magic_num(num):
    magic_num = False
    map_table = []  # In case the number repeats itself.
    
    while num > 1:
        print('Sequence --> ', num)
        
        val = square_of_square(num)
        
        if val == 1:
            map_table.append(num)
            magic_num = True
            break  
        else:
            if num in map_table:
                break
            else:
                map_table.append(num)
                num = val
    print(map_table)
    if magic_num is True:
        return 'Magic Number'
    else:
        return 'Not a magic number'

    
num = 18
status = perform_magic_num(num)
print(status)
