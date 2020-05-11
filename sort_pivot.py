''' Write a program that takes an array and index i into A  and rearranges the elements such 
    that all elements less that A[i]  appears before pivot , the pivot appears and 
    element > A[i] appears after pivot '''

def rearrange(num_arr, pivot_index):
    pivot = num_arr[pivot_index]
    len_num_arr  = len(num_arr)
    smaller = 0
    larger = len_num_arr - 1 
    
    # First Pass : Group elements less than pivot
    for i in range(len_num_arr):
        if num_arr[i] < pivot:
            num_arr[i], num_arr[smaller] = num_arr[smaller] , num_arr[i]
            smaller +=1

    # Second Pass : Group elements greater than pivot      
    for i in reversed(range(len_num_arr)):
        if num_arr[i] > pivot:
            num_arr[i], num_arr[larger] = num_arr[larger] , num_arr[i]
            larger -=1 

    return num_arr

if __name__ =='__main__':
    print('Re-arranged list is {}' .format(rearrange([0,1,2,0,2,1,1,3,3], 2)))