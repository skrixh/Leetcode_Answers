class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

# this is where the code starts
        ret = []     # creating an empty cell for o/p

        for i in range (1,n+1):     # here the looping starts with 1 and it should be n+1.
            if i % 3 == 0 and i % 5 == 0:      # using if else statement
                ret.append ("FizzBuzz")      # appending the values in ret
            elif i % 3 == 0:
                ret.append ("Fizz")
            elif i % 5 == 0:
                ret.append ("Buzz")
            else:
                ret.append (str(i))     # printing the elements of else as str.

        return ret      # returning the ret for o/p
