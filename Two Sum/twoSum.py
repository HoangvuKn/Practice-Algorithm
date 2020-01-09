from typing import List
class Solution:
    ## brute force
    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            left = nums[i+1:]
            for j in range(len(left)):
                if(nums[i] + left[j]) == target:
                    return i, j+1

    ## new brute force
    def twoSum_bf_new(self, nums: List[int], target: int) -> List[int]:
        k = 0
        for i in nums:
            k += 1
            if (target - i) in nums[k:]:
                return (k-1, nums[k:].index(target - i) + k)
    
    ## two hash table
    def twoSum_2HashTable(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} 
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hash_table:
                if hash_table[target-nums[i]] != i:
                    return [i, hash_table[target-nums[i]]]
        return []
    
    ## one pass table
    def twoSum_onePassTable(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target-num], i])
            hash_table[num] = i
        
        return []
s = Solution()
print(s.twoSum_onePassTable([2, 7, 11, 15], 9))