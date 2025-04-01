#1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

    # from this the main code starts
        sums = 0    # [0->1, 1->3, 3->6, 6->10] 
        sums_arr = []  # empty list used for o/p

        for i in range (len(nums)):    #determing the len(nums) and for looping those len
            sums += nums[i] # since it is looping the index num of nums will be changed and added like (sums + nums(0))
            sums_arr.append(sums) #using the sums answer it'll be appended in the sum_arr. 
        
        return sums_arr. # then it will be returned for o/p 
