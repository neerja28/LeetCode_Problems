#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321

#Example 2:

#Input: -123
#Output: -321

#Example 3:
#Input: 120
#Output: 21

#Note:
#Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this 
# problem, assume that your function returns 0 when the reversed integer overflows.


# Solution

Number    Reverse  Reminder     Formula
1234         0       4 (num%10)  reverse * 10 + num % 10 = 4
num //10
123          4       3             43
12           43      2             432
1            432     1             4321

class Solution:
    def reverse(self, x):
        
        max_int = 2147483647
        min_int = -2147483647
    
        if (x > max_int) or (x < min_int):
            return 0
        else:
            x = abs(x)
            reverse_num = 0
            sign = (x > 0) - (x < 0) # Will return 1 or -1 
            while (x != 0):
                reminder = x % 10
                x = x // 10
                reverse_num = reverse_num * 10 + reminder
            
            if (reverse_num > max_int) or (reverse_num < min_int):
                return 0
            
            return reverse_num * sign
            
