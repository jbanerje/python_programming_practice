''' return prime numbers between 1 and n '''
''' Reference : https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python/39106237#39106237'''

def find_prime_num(num):
    prime_num_list = []
    sieve = [True] * (num + 1)
    for i in range(2, num + 1):
        if (sieve[i]):
            prime_num_list.append(i)
            for i in range(i, num + 1, i):
                sieve[i] = False
    return prime_num_list

def brute_force_find_prime_num(num):
    prime_num_list = [];count=0

    for num in range(2, num+1):
        for den in range(2, num+1):
            if num % den == 0:
                count += 1
        if count == 1:
            prime_num_list.append(num)
        count=0

    return prime_num_list

if __name__ == "__main__":
    # print('prime numbers b/w 1 and {} are {}'.format(10, brute_force_find_prime_num(10)))
    print('prime numbers b/w 1 and {} are {}'.format(10, find_prime_num(10)))