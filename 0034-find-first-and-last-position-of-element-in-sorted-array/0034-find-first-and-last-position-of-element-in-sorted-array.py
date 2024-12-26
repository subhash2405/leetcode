from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start(nums, target):
            low, high = 0, len(nums) - 1
            start = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    start = mid
                    high = mid - 1  # Search in the left half
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return start

        def find_end(nums, target):
            low, high = 0, len(nums) - 1
            end = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    end = mid
                    low = mid + 1  # Search in the right half
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return end

        start = find_start(nums, target)
        end = find_end(nums, target)
        return [start, end]
