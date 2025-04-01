class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
    
      # from here the code starts
      
        richest_wealth = 0  # let us create a smaple set for o/p

        for cus_acc in accounts:      # using a for loop we'll be looping the accounts with cus_acc. 
            cus_wealth = sum(cus_acc)      # creating a new one called cus_wealth and adding the elements inside the cus_acc to this. 
            richest_wealth = max(richest_wealth, cus_wealth)    #now finding the max of both the elements. 
        return richest_wealth       #returning the max element stored in the richest_wealth.
