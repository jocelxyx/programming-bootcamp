"""
This program aims to display the digits inside a list as a single number.

Firstly, a function called convert_list is defined. Inside the function, a variable called 'result' is declared. 
This variable acts like a storage, a place to store the output of each iteration. 
There is also a for loop inside the function, which iterates through every digit in the list, from left to right.
The loop will end when it reaches the end of the list.

How the code works:
In the loop, we use a formula which multiplies the current value of 'result' by 10 and it to the current digit being iterated.
Since there are four digits in the list, the 1st element is the thousandth, followed by 2nd element as hundreds, 3rd element as tenths, and lastly, ones.
This also applies for lists with less or more digits. Basically, the smaller the index of a digit in a list, the higher its value, with the last digit always as ones.

In order to display all the numbers as an integer, we firstly add the first digit to 'result', and then multiplies it by 10 so its value increases by 10 times each time.
We do this for all the digits inside the list using for loop and store the output each time in 'result'. The final result will then be all the digits inside the list as an integer.

To understand the program better, we will look at the explanation below:
lst1 = [8,3,5,1]

First iteration:
result = (0 * 10) + 8 = 8

Second iteration:
result = (8 * 10) + 3 = 83

Third iteration:
result = (83 * 10) + 5 = 835

Last iteration:
result = (835 * 10) + 1 = 8351

Then, we call the function, which returns 8351 as the output
"""

# function to convert all the digits inside a list to an integer
def convert_list(lst):
    # declare and assign value to the variable 'result'
    result = 0

    # iterate through each element of the list
    for i in lst:
        result = (result * 10) + i
        
    return result

# test cases
lst1 = [8,3,5,1]
lst2 = [1,2,3,4]

# call the function and print the output
print(convert_list(lst1))
print(convert_list(lst2))