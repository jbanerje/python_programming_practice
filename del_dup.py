''' Delete Duplicates from sorted Array '''

def remove_dup(dup_arr):
    unq_arr = []
    for val in dup_arr:
        if val not in unq_arr:
            unq_arr.append(val)
    return unq_arr

if __name__ == "__main__":
    print('Unique array - {}'.format(remove_dup([1,1,2,3,4,4,5,6,6])))
