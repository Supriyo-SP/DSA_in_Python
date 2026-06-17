class Solution(object):
    def divide(self, dividend, divisor):
        # 1. Define the 32-bit integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # 2. Handle the specific overflow edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # 3. Determine the sign of the result using XOR
        # True if one is negative and the other is positive, False otherwise
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # 4. Work with absolute positive values
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # 5. Exponential subtraction using bit manipulation
        # We loop from 31 down to 0 because 31 is the max bit-shift for a 32-bit int
        for i in range(31, -1, -1):
            # Check if (abs_divisor * 2^i) fits into the remaining dividend
            if (abs_dividend >> i) >= abs_divisor:
                # Add 2^i to the quotient
                quotient += (1 << i)
                # Subtract (abs_divisor * 2^i) from the dividend
                abs_dividend -= (abs_divisor << i)
                
        # 6. Apply the proper sign to the final answer
        if is_negative:
            quotient = -quotient
            
        return quotient