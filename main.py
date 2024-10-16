# No. 1
fruits = ["banana", "cherry", "\napple\n", "watermelon"]
print(fruits[2])

print("-----------------------------------")

# No. 2
import array

numbers = array.array('i', [10, 20, 30, 40, 50])

total_sum = sum(numbers)

average = total_sum / len(numbers)

maximum_value = max(numbers)

# Print the results
print(f"\nSum: {total_sum}")
print(f"Average: {average}")
print(f"Maximum Value: {maximum_value}\n")

print("-----------------------------------\n")


# No. 3

mixed_data_types = ["banana", 23, True, False, "Nash", 3.14, "HardWare"]
print(len(mixed_data_types))


# No. 4

print("\n-----------------------------------")


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr_squared = arr ** 2

arr_sum = np.sum(arr)
arr_mean = np.mean(arr)



print("Array:", arr)
print("Squared:", arr_squared)
print("Sum:", arr_sum)
print("Mean:", arr_mean)


# What are the key differences between lists and arrays in Python?

'''
The key difference between lists and arrays in Python is that lists can store elements of any data type,
while arrays are typically limited to a single data type. Additionally, both lists and arrays are mutable,
meaning you can modify their contents after creation. This includes operations such as adding,
removing, or changing elements.
'''

# When is it appropriate to use a list and when is it better to use an array?

'''
 Use a list when you need flexibility in storing elements of different data types, as lists can hold
 integers, strings, objects, and more in a single collection. They are ideal for general-purpose
 programming, especially when the dataset is small or the types of data vary significantly.
 On the other hand, opt for arrays, particularly NumPy arrays, when working with large datasets of 
 numerical data where performance and efficiency are crucial. Arrays are more memory-efficient and 
 faster for numerical operations, as they support a wide range of mathematical functions and optimized 
 computations. Additionally, arrays offer advanced capabilities like multi-dimensional structures and 
 broadcasting, making them more suitable for scientific computing, data analysis, and mathematical 
 modeling.
'''

# What are the advantages of using NumPy arrays for numerical operations?

'''
NumPy arrays are great for numerical operations for several reasons. 
First, they are much faster than Python lists, especially when working with large amounts of data, 
because they are built in C. They also use memory more efficiently since they store all elements
of the same type together. NumPy can easily handle multi-dimensional data, like matrices, 
which is useful for things like math and image processing. It offers a lot of 
built-in mathematical functions, making calculations simpler. Plus, with features like broadcasting, 
you can perform operations on different-shaped arrays without extra steps. Overall, NumPy makes it 
easier and faster to work with numbers in Python, especially for data analysis and scientific work.
'''


