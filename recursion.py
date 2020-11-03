"""Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer."""

def calc_digits(x):
    result = sum(list(map(int,str(x))))
    
    if len(str(result))==1:
        return result
    else:
        return calc_digits(result) 

print(calc_digits(1234))