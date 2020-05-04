'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def check_two_sum(nums, target):
    ''' Time Complexity - O(n) '''
    complement_list = [target-nums[i] for i in range(len(nums))]
    final_list = [i for i in range(len(nums)) if nums[i] in complement_list]
    return final_list

def check_two_sum_brute_force(nums, target):
    ''' Time Complexity - O(n^2) '''
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums), 1):
            if (nums[i] + nums[j]) == target:
                result.append([i, j])
    return result

if __name__ == "__main__":
    result = check_two_sum_brute_force([3, 2, 4], 6)
    print(result[0])

    result1 = check_two_sum([3, 2, 4], 6)
    print(result1)




