# 📊 Data Analyzer and Transformer Program

## 📌 Project Description

The **Data Analyzer and Transformer Program** is a Python-based menu-driven application designed to input, analyze, filter, sort, and calculate statistics from datasets.

This project demonstrates several important Python programming concepts, including:

- 1D and 2D Arrays (Lists)
- Built-in Functions
- Recursion
- Lambda Functions
- Sorting
- Functions Returning Multiple Values
- Menu-Driven Programming
- Loops
- Conditional Statements

---

# 🚀 Features

The program provides the following options:

1. **Input Data**
2. **Display Data Summary**
3. **Calculate Factorial**
4. **Filter Data by Threshold**
5. **Sort Data**
6. **Display Dataset Statistics**
7. **Exit Program**

---

# 📋 Main Menu

```text
Main Menu:

1. InputData
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Please enter your choice number:
```

---

# 🔹 1. Input Data

The **Input Data** option allows the user to enter data using either a **1D array** or a **2D array**.

## 1D Array

The user can enter a collection of values into a one-dimensional list.

## 2D Array

The user can specify:

- Number of rows
- Number of columns
- Values for each position

### Example

```text
Please Enter Your Choice Number 1 & 2: 2

Enter Data for a 2D array rows: 2
Enter Data for a 2D array cols: 2

enter the number 1
enter the number 2
enter the number 3
enter the number 4

Successfully data input for 2D array:
[[1, 2], [3, 4]]
```

---

# 🔹 2. Display Data Summary

This option displays a summary of the dataset using Python's built-in functions.

The program calculates:

- Total number of values
- Minimum value
- Maximum value
- Sum of all values
- Average value

### Example Output

```text
Display Data Summary of The Dataset Using Built-in functions.

Data Summary

Total Value :- 4
Minimum Value :- 1
Maximum Value :- 4
Sum of all Value :- 10
Average Value :- 2.5
```

### Built-in Functions Used

```python
len()
min()
max()
sum()
```

---

# 🔹 3. Calculate Factorial

This option calculates the factorial of a number using **recursion**.

### Example

```text
Calculate factorial of a number using recursion

Enter your factorial number: 4

Factorial of 4 is: 24
```

### Factorial Calculation

```text
4! = 4 × 3 × 2 × 1
   = 24
```

### Example Recursive Function

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

---

# 🔹 4. Filter Data by Threshold

This option filters the dataset based on a specified threshold value.

A **lambda function** is used to perform the filtering operation.

### Example

```text
Enter a threshold value to filter out data above this value: 10

Data filtered by threshold (value >=10):
```

### Lambda Concept

```python
lambda x: x >= threshold
```

This allows the program to select values that satisfy the specified condition.

---

# 🔹 5. Sort Data

This option allows the user to sort the dataset.

The user can choose between:

1. Ascending Order
2. Descending Order

### Example

```text
Sorting the data in ascending or descending order.

Choose sorting option:

1. Ascending
2. Descending

Enter your choice number: 2

Sorted Data in Descending Order:
[[3, 4], [1, 2]]
```

### Sorting Functions

Ascending:

```python
sorted(data)
```

Descending:

```python
sorted(data, reverse=True)
```

---

# 🔹 6. Display Dataset Statistics

This option uses a `dataset_statistics()` function that returns multiple values.

The function calculates:

- Minimum value
- Maximum value
- Sum of all values
- Average value

### Example Output

```text
Display dataset statistics using the dataset_statistics function.

Dataset Statistics:

Minimum Value: 1
Maximum Value: 4
Sum of all values: 10
Average Value: 2.5
```

### Multiple Return Values

```python
def dataset_statistics(data):
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average
```

---

# 🔹 7. Exit Program

This option terminates the program.

### Example

```text
Exiting the program:
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Programming Language |
| **Lists** | 1D and 2D Data Storage |
| **Built-in Functions** | Data Analysis |
| **Recursion** | Factorial Calculation |
| **Lambda Function** | Data Filtering |
| **`sorted()`** | Data Sorting |
| **Functions** | Program Organization |
| **Loops** | Menu Control |
| **Conditional Statements** | User Choice Handling |

---

# 📂 Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── main.py
├── output.png
└── README.md
```

---

# 📸 Program Output

The following image shows the output of the program:

![Program Output](output.png)

---

# 🧪 Sample Execution

## Input Data

```text
Please enter your choice number : 1

using 1D array and 2D array to input data

Please Enter Your Choice Number 1 & 2: 2

Enter Data for a 2D array rows: 2
Enter Data for a 2D array cols: 2

enter the number 1
enter the number 2
enter the number 3
enter the number 4

Successfully data input for 2D array:
[[1, 2], [3, 4]]
```

## Data Summary

```text
Please enter your choice number : 2

Data Summary

Total Value :- 4
Minimum Value :- 1
Maximum Value :- 4
Sum of all Value :- 10
Average Value :- 2.5
```

## Factorial

```text
Please enter your choice number : 3

Calculate factorial of a number using recursion

Enter your factorial number: 4

Factorial of 4 is: 24
```

## Filter Data

```text
Please enter your choice number : 4

Enter a threshold value to filter out data above this value: 10

Data filtered by threshold (value >=10):
```

## Sorting

```text
Please enter your choice number : 5

Sorting the data in ascending or descending order.

Choose sorting option:

1. Ascending
2. Descending

Enter your choice number: 2

Sorted Data in Descending Order:
[[3, 4], [1, 2]]
```

## Dataset Statistics

```text
Please enter your choice number : 6

Display dataset statistics using the dataset_statistics function.

Dataset Statistics:

Minimum Value: 1
Maximum Value: 4
Sum of all values: 10
Average Value: 2.5
```

## Exit

```text
Please enter your choice number : 7

Exiting the program:
```

---

# ▶️ How to Run

## Step 1: Install Python

Make sure **Python 3** is installed on your computer.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

---

## Step 3: Open the Project Directory

```bash
cd Data-Analyzer-and-Transformer
```

---

## Step 4: Run the Program

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

# 🎯 Learning Objectives

This project demonstrates the practical use of fundamental Python concepts.

By completing this project, you can understand:

- How to create menu-driven programs
- How to store data in 1D arrays
- How to store data in 2D arrays
- How to use Python built-in functions
- How recursion works
- How lambda functions can be used for filtering
- How to sort data
- How functions can return multiple values
- How loops work
- How conditional statements work
- How to perform basic dataset analysis

---

# 📊 Example Dataset

The program can work with a dataset such as:

```python
[[1, 2],
 [3, 4]]
```

The values are:

```text
1, 2, 3, 4
```

### Dataset Statistics

| Statistic | Result |
|---|---:|
| Total Values | 4 |
| Minimum | 1 |
| Maximum | 4 |
| Sum | 10 |
| Average | 2.5 |

---

# ⚠️ Important Notes

- Enter numeric values when entering dataset values.
- Enter a valid integer when calculating factorial.
- Menu choices should be between `1` and `7`.
- The threshold value should be numeric.
- The dataset should contain numeric values for statistical calculations.

---

# 💡 Future Improvements

Possible future improvements include:

- Save dataset to a file
- Load dataset from a file
- CSV file support
- Data visualization
- Median and mode calculations
- Standard deviation calculation
- Error handling for invalid input
- Support for larger datasets
- Export statistics to a file
- Graphical User Interface (GUI)

---

# 👨‍💻 Author

**Data Analyzer and Transformer Program**

A Python project created to demonstrate fundamental Python programming concepts and basic data analysis techniques.

---

# 📜 License

This project is created for educational and learning purposes.
