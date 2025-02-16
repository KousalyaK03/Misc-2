# Approach:
# We use a modified binary search to efficiently locate the given string in a sorted array interspersed with empty strings.
# If the middle element is an empty string, we search for the nearest non-empty string in either direction.
# If the middle element is the target, return its index.
# Otherwise, continue binary search in the appropriate half of the array.

# Time Complexity: O(log n) in the best case (when there are few empty strings), but it can degrade to O(n) if many empty strings exist.
# Space Complexity: O(1), since we use a constant amount of extra space.

class Solution:
    def sparseSearch(self, arr: List[str], x: str) -> int:
        left, right = 0, len(arr) - 1  # Initialize binary search bounds

        while left <= right:
            mid = (left + right) // 2  # Compute middle index

            # If mid is an empty string, find the closest non-empty string
            if arr[mid] == "":
                left_idx, right_idx = mid - 1, mid + 1
                
                # Search towards both left and right for the closest non-empty string
                while True:
                    if left_idx < left and right_idx > right:  # If both sides are out of bounds
                        return -1
                    elif right_idx <= right and arr[right_idx] != "":
                        mid = right_idx  # Update mid to closest non-empty string
                        break
                    elif left_idx >= left and arr[left_idx] != "":
                        mid = left_idx  # Update mid to closest non-empty string
                        break
                    right_idx += 1
                    left_idx -= 1

            # Perform standard binary search comparison
            if arr[mid] == x:
                return mid  # Found target, return index
            elif arr[mid] < x:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return -1  # Target not found
