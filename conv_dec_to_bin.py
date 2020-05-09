# Convert Decimal to Binary

def validate_binary(binary_num_eqv):
    validated_dec=0 ;count = 0
    while binary_num_eqv > 0:
        validated_dec += (2**count) * (binary_num_eqv % 10)
        count += 1
        binary_num_eqv = int(binary_num_eqv / 10)
    return validated_dec

def convrt_dec_bin(num):
    binary_num = [] ; sum=0;  actual_num = num
    
    # Get the remainders in a list
    while num > 0:
        binary_num.append(num % 2)
        num = int(num/2)

    # Have the binary equivalent from the list
    for i in range(len(binary_num)):
        sum += binary_num[i] * (10**i)

    # Binary Validation with decimal numner
    validated_dec = validate_binary(sum)
    if  validated_dec == actual_num :
        return sum
    else:
        return('Failed!')

if __name__=='__main__':
    num = 10
    print('Binary equivalent of {} is {}'.format(num, convrt_dec_bin(num)))
    