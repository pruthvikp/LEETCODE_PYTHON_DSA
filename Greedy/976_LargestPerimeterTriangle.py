'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 
Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
'''

# Approach:
# 1)If the side of a triangle are a,b,c then a+b>c for the triangle to be formed .
# 2)Sort the array to get the maximum element of the array at a side ;
# 3)Traverse the array bacckward to find nums[i]<nums[i-1]+nums[i-2] till the index 2 as i-2 will get out of bound ,
# 4)Store the value of it in ans (default value is 0) and return it .

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
