Data Analyzer and Transformer Program

A menu-driven Python program that allows users to input numerical data and perform different data analysis and transformation operations.

The project demonstrates important Python programming concepts such as lists, nested lists, functions, recursion, lambda functions, built-in functions, filtering, sorting, and returning multiple values from a function.

Features

The program provides the following features:

1. Input Data

The program supports two types of data input:

1D Array

2D Array

1D Array Example

The user can enter multiple numbers separated by spaces:

Please Enter Your Choice Number 1 & 2: 1
Enter Data for a 1D array (separated by Spaces): 10 20 30 40


The data is stored as:

[10, 20, 30, 40]

2D Array Example

The user specifies the number of rows and columns:

Please Enter Your Choice Number 1 & 2: 2
Enter Data for a 2D array rows: 2
Enter Data for a 2D array cols: 2


Example data:

[[1, 2], [3, 4]]

2. Display Data Summary

The program uses Python's built-in functions to calculate information about the dataset.

The following values are displayed:

Total number of values

Minimum value

Maximum value

Sum of all values

Average value

Example:

Data Summary
Total Value :- 4
Minimum Value :- 1
Maximum Value :- 4
Sum of all Value :- 10
Average Value :- 2.5


The program uses built-in functions such as:

len()
min()
max()
sum()

3. Calculate Factorial

The program calculates the factorial of a number using recursion.

Example:

Enter your factorial number: 4
Factorial of 4 is: 24


The recursive function is:

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

4. Filter Data by Threshold

The program uses a lambda function together with Python's filter() function.

The user enters a threshold value, and values greater than the threshold are displayed.

Example:

Enter a threshold value to filter out data above this value: 2
Data filtered by threshold (value >=2):
3 , 4


The filtering operation uses:

filter(lambda a: a > thr, l)

5. Sort Data

The program provides two sorting options:

1. Ascending
2. Descending


Python's sorted() function is used for sorting.

Ascending Order
sorted(data)


Example:

Sorted Data in Ascending Order:
[[1, 2], [3, 4]]

Descending Order
sorted(data, reverse=True)

6. Display Dataset Statistics

The dataset_statistics() function calculates and returns multiple values.

The returned values are:

Minimum value

Maximum value

Total/sum

Average

Example:

Dataset Statistics:
Minimum Value: 1
Maximum Value: 4
Sum of all values: 10
Average Value: 2.5


The function returns multiple values using:

return minimum, maximum, total, average


These values are then stored using multiple assignment:

minimum, maximum, total, average = dataset_statistics()

7. Exit Program

Option 7 exits the program:

Exiting the program:

Data Conversion

The program contains a converter() function that converts a 2D list into a 1D list.

For example:

[[1, 2], [3, 4]]


is converted to:

[1, 2, 3, 4]


This allows the same analysis functions to work with both 1D and 2D data.

The function checks whether the first element is a list:

if len(data) > 0 and isinstance(data[0], list):


If the data is 2D, the nested lists are combined using extend().

Technologies Used

Python 3

Python Lists

Nested Lists

Functions

Global Variables

len() function

min() function

max() function

sum() function

filter()

Lambda functions

sorted()

Recursion

Multiple return values

input() and console output

Project Structure
project4/
│
├── main.py
└── README.md
└── output.png

##  output

![Program Output](output.png)



Requirements

The project requires:

Python 3.x

You can check whether Python is installed using:

python --version

How to Run

Open PowerShell or Command Prompt and navigate to the project directory:

cd D:\project4


Run the program:

python main.py

Main Menu

When the program starts, the following menu is displayed:

Main Menu:

1. InputData
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. sort Data
6.Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Example Execution

For a 2D dataset:

[[1, 2], [3, 4]]

Data Summary
Total Value :- 4
Minimum Value :- 1
Maximum Value :- 4
Sum of all Value :- 10
Average Value :- 2.5

Factorial

For input 4:

Factorial of 4 is: 24

Sorting

Ascending:

[[1, 2], [3, 4]]

Dataset Statistics
Minimum Value: 1
Maximum Value: 4
Sum of all values: 10
Average Value: 2.5

Python Concepts Demonstrated

This project is designed to demonstrate the following concepts:

Concept	Implementation
1D Array	Python list
2D Array	Nested Python lists
Built-in Functions	len(), min(), max(), sum()
Recursion	Factorial calculation
Lambda Function	Threshold filtering
Filter	filter()
Sorting	sorted()
Functions	Separate functions for each operation
Multiple Return Values	dataset_statistics()
Type Checking	isinstance()
User Input	input()
Menu System	while True loop and if/elif
Functions

The program contains the following functions:

input_data()
converter(data)
data_summary()
fact(n)
factorial()
threshold_data()
sort_data()
dataset_statistics()

input_data()

Accepts 1D or 2D numerical data from the user.

converter(data)

Converts 2D data into a flat 1D list for analysis.

data_summary()

Displays basic information about the dataset using built-in functions.

fact(n)

Recursively calculates the factorial of a number.

factorial()

Gets a number from the user and displays its factorial.

threshold_data()

Filters values using a lambda function.

sort_data()

Sorts the dataset in ascending or descending order.

dataset_statistics()

Calculates and returns minimum, maximum, sum, and average values.

Conclusion

The Data Analyzer and Transformer Program is a simple Python-based application for practicing fundamental programming concepts and basic data processing.

It combines multiple Python techniques into one menu-driven program, making it useful for learning:

Data input and storage

Data transformation

Data analysis

Functional programming concepts

Recursion

Sorting

Python functions

Console-based application development

Author

Data Analyzer and Transformer Program

Developed as a Python programming project for practicing fundamental Python programming and data analysis concepts.