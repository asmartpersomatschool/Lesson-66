#A Python program that finds the longest continuous run of 1s in a binary list using a streak counter that resets on 0 and a best tracker that stores the highest streak.
def longest_run_of_ones(binary_list):
    best_streak = 0
    current_streak = 0
    for num in binary_list:
        if num == 1:
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
        else:
            current_streak = 0        
    return best_streak
nums = [1, 1, 0, 1, 1, 1, 0, 1]
print(f"Longest run of 1's: {longest_run_of_ones(nums)}")
#A Python program that moves all zeros to the end of a list using a write pointer, keeping all non-zero values at the front and filling the remaining positions with zeros.
def move_zeros_to_end(nums):
    write_pointer = 0
    for current_val in nums:
        if current_val != 0:
            nums[write_pointer] = current_val
            write_pointer += 1
    while write_pointer < len(nums):
        nums[write_pointer] = 0
        write_pointer += 1
    return nums
nums = [0, 1, 0, 3, 12, 0, 9]
print(f"Modified list: {move_zeros_to_end(nums)}")
#A Python program that finds the longest continuous run of 0s in a binary list using a streak counter that resets on 1 and a best tracker that keeps the maximum streak found.
def longest_run_of_zeroes(binary_list):
    best_streak = 0
    current_streak = 0
    for num in binary_list:
        if num == 0:
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
        else:
            current_streak = 0
    return best_streak
nums = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1]
print(f"Longest run of 0's: {longest_run_of_zeroes(nums)}")