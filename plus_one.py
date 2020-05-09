'''Plus One https://leetcode.com/problems/plus-one/'''
def plus_one(arr):
    sum=0 ; arr_len = len(arr)
    for index, data in enumerate(arr):
        sum += (data * 10 **(arr_len-index-1))
    return [i for i in str(sum+1)]

if __name__ == "__main__":
    print('Plus One Inter-{}'.format(plus_one([9])))