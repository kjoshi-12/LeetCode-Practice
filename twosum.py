#Problem: Two Sum
#Description: For a list, find the two elements that add up to a target and return their indices in a 2 element list

def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = [0,0]
        n = len(nums)
        
        for i in range(n-1):
            for j in range((i + 1),n):
                if(nums[i] + nums[j] == target):
                    indices[0] = i
                    indices[1] = j
        return indices
