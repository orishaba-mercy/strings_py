# Write a Python program that takes a list of strings 
# as input and outputs the number of times each string 
# appears in the list, using a dictionary and conditional statements.
def words(word):
    empty={}
    for i in word:
        if i in empty:
            empty[i]+=1
    else:
            empty[i]=1
    return empty
word =["mum","mercy","hopperlab","mum"]
results=words(word)
print(results)

# Write a Python program that takes a list of numbers 
# as input and outputs the median of the numbers 
def median_numbers(nums):
     sum=1
     sum+=nums
     nums/len(nums%2)
print(median_numbers(nums))
nums=[1,2,3,4,5,6]
median_numbers(nums)


# Write a Python program that takes a list of numbers
#  as input and outputs the second largest number in the 
# list using conditional statements and a for loop.
numbers = [3, 7, 1, 8, 4, 9, 2]
secordlargest = sorted(numbers, reverse=True)[1]
print(secondlargest)

# Write a Python program that takes a year as input and 
# determines if it is a leap year.
def lep():
        if year % 400 == 0:
            print(year, "is a leap year")
        elif year % 100 == 0:
            print(year, "is not a leap year")
        elif year % 4 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")


# Write a Python program that takes a string as input and 
# checks if it is a palindrome (reads the same forwards and backwards),
#  ignoring spaces and punctuation.