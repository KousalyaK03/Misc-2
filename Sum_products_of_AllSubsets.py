# Approach:
# Instead of generating all subsets explicitly, we use a mathematical approach to compute the sum of products efficiently.
# Each element contributes to half of the subsets, so we use the formula:
# Total Sum = (1 + a1) * (1 + a2) * ... * (1 + an) - 1
# This formula expands into all subset products plus 1 (empty subset), so we subtract 1 to exclude it.

# Time Complexity: O(n), since we iterate through the array once.
# Space Complexity: O(1), as we use only a single variable to store the result.

class Solution:
    def subsetProductSum(self, arr: List[int]) -> int:
        total_product_sum = 1  # Initialize the total product sum

        # Multiply (1 + element) for each element in the array
        for num in arr:
            total_product_sum *= (1 + num)
        
        return total_product_sum - 1  # Subtract 1 to remove the empty subset
