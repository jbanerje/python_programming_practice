'''Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/ '''

def remove_dup_inplace(arr):
    for i, data in enumerate(arr):
        while data in arr[i+1:len(arr)]:
            data_index = arr[i+1:len(arr)].index(data)
            arr.pop(data_index + i + 1)
    return arr, len(arr)
            
def remove_dup_brute_force(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])

    return new_arr, len(new_arr)

if __name__=="__main__":
    arr = [0,0,1,1,1,2,2,3,3,4]
    # new_arr, len_new_arr = remove_dup_brute_force(arr)
    # print('New Array={}, Length-{}'.format(new_arr, len_new_arr))
    new_arr, len_new_arr = remove_dup_inplace(arr)
    print('New Array={}, Length-{}'.format(new_arr, len_new_arr))
    