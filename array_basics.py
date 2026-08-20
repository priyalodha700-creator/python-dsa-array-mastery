# Array Basics: Common Operations & Fundamental Problems

def find_min_max(arr):
    """Find Minimum and Maximum element in an array"""
    if not arr:
        return None, None
    
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val


def reverse_array(arr):
    """Reverse an array in-place using Two Pointers"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def find_second_largest(arr):
    """Find the second largest unique element in an array"""
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None


# Driver Code for Testing
if __name__ == "__main__":
    nums = [12, 35, 1, 10, 34, 1]
    
    print("Original Array:", nums)
    print("Min & Max:", find_min_max(nums))
    print("Second Largest:", find_second_largest(nums))
    print("Reversed Array:", reverse_array(nums.copy()))
