# Array Algorithms: Important Interview Questions

def two_sum(nums, target):
    """Two Sum using Hash Map - O(n) Time Complexity"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def kadanes_algorithm(nums):
    """Kadane's Algorithm for Maximum Subarray Sum - O(n)"""
    max_so_far = nums[0]
    current_max = nums[0]
    
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far


def move_zeroes(nums):
    """Move all 0s to the end while maintaining relative order - In-Place"""
    write_ptr = 0
    
    for read_ptr in range(len(nums)):
        if nums[read_ptr] != 0:
            nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
            write_ptr += 1
            
    return nums


# Driver Code for Testing
if __name__ == "__main__":
    # Two Sum Test
    arr1 = [2, 7, 11, 15]
    print("Two Sum Indices (Target 9):", two_sum(arr1, 9))
    
    # Kadane's Test
    arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", kadanes_algorithm(arr2))
    
    # Move Zeroes Test
    arr3 = [0, 1, 0, 3, 12]
    print("Array after Moving Zeroes:", move_zeroes(arr3))
