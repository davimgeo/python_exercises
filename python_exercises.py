#Write a Python program to sum all the items in a list.
numbers = [8, 4, 10, 2, 6]

n = len(numbers)
def sum_all(numbers):
    dum = 0.0
    for i in range(n):
        dum += numbers[i]
    return dum
#print(sum_all(numbers))
#Write a Python program to multiply all the items in a list.
dum1 = 1.0
def multiply_all(dum1):
    for i in range(n):
        dum1 *= numbers[i]
    return dum1
#print(multiply_all(dum1))
# Write a Python program to get the largest number from a list.
dum2 = 0.0
def largest_number(dum2):
    for i in range(n-2):
        if numbers[i] > numbers[i+1]:
            dum2 = numbers[i]
        if numbers[i] < numbers[i+1]:
            dum2 = numbers[i+1]
    return dum2
#print(largest_number(dum2))
#Write a Python program to get the smallest number from a list.
min_num = numbers[0]
def smallest_number(min_num):
    for element in numbers:
        if element < min_num:
            min_num = element
    return min_num
#print(smallest_number(min_num))
# Write a Python program to get a list, sorted in increasing order by the last element 
#in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]   

tupl3_array = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

crescent_tuple = []
for _ in range(len(tupl3_array)):
    min_tuple = tupl3_array[0]
    for elements in tupl3_array:
        if elements[1] < min_tuple[1]:
            min_tuple = elements

    crescent_tuple.append(min_tuple)
    tupl3_array.remove(min_tuple)



#print(crescent_tuple)
#Write a Python program to remove duplicates from a list.
duplicate_array = [1, 2, 4, 2, 1]

i = 0
while i < len(duplicate_array):
    element = duplicate_array[i]
    if duplicate_array.count(element) > 1:
        duplicate_array.remove(element)
    else:
        i += 1

#print(duplicate_array)
#Write a Python program to check if a list is empty or not.
empty_list = []

def check_empty(empty) -> None:
    if not empty_list:
        print(f"your list is empty.")
    else:
        print(f"your list is not empty")

#check_empty(empty_list)
#Write a Python program to clone or copy a list.
random_list = ['a', 2, 'feijão', 4, 5]

copy_list = []
for elements in random_list:
    copy_list.append(elements)
    
#Write a Python program to find the list of words that are longer than n from a given list of words.
words_list = ['lumah', 'davi', 'coração', 'kuromi', 'filha']

i = 5
long_words = [elements for elements in words_list if len(elements) > i]
#Write a Python function that takes two lists and returns True if they have at least one common member.
equal_list = [20, 2, 23, 4, 25]
equal_list2 = [10, 3, 5, 7, 9]

def check_commom_member(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return print("True")
    return print("There's no common member between lists")          

#check_commom_member(equal_list, equal_list2)   
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']        
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

Sample_List = [x for (i, x) in enumerate(Sample_List) if i not in (0, 4, 5)]

#print(Sample_List)
#Write a Python program to generate a (3, 4, 6) 3D array whose each element is *.
dim1 = 3
dim2 = 4
dim3 = 5

array_3d = [[[0 for k in range(dim3)] for j in range(dim2)] for i in range(dim1)]

#print(array_3d)
#Write a Python program to print the numbers of a specified list after removing even numbers from it
even_list = [1, 2, 3, 4, 5]

even_list = [i for i in even_list if i %2 != 0]

#print(even_list)
#Write a Python program to shuffle and print a specified list.
from random import shuffle
shuffled_list = [1, 2, 3, 4, 5]

shuffle(shuffled_list)

#print(shuffled_list)
#Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
square_numbers_list = []

for i in range(1, 31):
    if (i**(1/2)).is_integer():
        square_numbers_list.append(i)

#print(square_numbers_list)
#Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
prime_list = [2, 3, 5, 7, 11]
not_prime_list = [1, 4, 6, 8, 9]

def check_prime(list1):
    for i in range(2, 11):
        test_list = []
        for number in list1:
            test_list.append(number%i)
        if test_list.count(0) > 1:
            print("False")
            break
        elif test_list.count(0) == 0:
            print("True")
            break

#check_prime(not_prime_list)
def is_prime(num):
    if num == 2 or num == 3: return True
    if num < 2 or not num % 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True

#print(is_prime(61))
#Write a Python program to generate all permutations of a list in Python
permutation_list = [1, 2, 3, 4, 5]

n = len(permutation_list)
def permutation_of_list(x):
    if x == 1: return 1
    return x * permutation_of_list(x - 1)

#print(permutation_of_list(n)) 
#Write a Python program to calculate the difference between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = []
def difference_two_arrays(list1, list2):
    for i in range(len(list1)):
        dif = list2[i] - list1[i]
        result.append(dif)
    return result

#print(difference_two_arrays(list1, list2)) 
#Write a Python program to access the index of a list
nums = [5, 15, 35, 8, 98]

def index_list(array):
    for num_index, num_val in enumerate(nums):
        print(num_index, num_val)

#index_list(nums)
#Write a Python program to convert a list of characters into a string.
char_list = ['a', 'b', 'c', 'd', 'e']

str1 = ''.join(char_list)

#print(str1)
#Write a Python program to find the index of an item in a specified list.
test_list = ['arroz', 'feijao', 'cebola', 'carne', 'tempero']

def find_intex(list1, word):
    return list1.index(word)

index_finder = find_intex(test_list, 'feijao')

#print(index_finder)
#Write a Python program to flatten a shallow list.
def flatten(nums):
    return [x for y in nums for x in y]
    
nums = [[1, 2, 3, 4], [5, 6, 7, 8]]

#print(flatten(nums))
#Write a Python program to select an item randomly from a list.

        