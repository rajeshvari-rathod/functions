
print("welcome to the Data Analyzer and Transformer Program")
data = []

def input_data():
    """using 1D array and 2D array to input data"""
    global data
    print("selected option: ")
    print("1D array: ")
    print("2D array: ")

    choice = int(input("Please Enter Your Choice Number 1 & 2: "))

    if choice == 1:
        """get the data for 1D array"""

        arr = input("Enter Data for a 1D array (separated by Spaces)").split()
        data = list(map(int,arr))
        print("Successfully data input for 1D array: ")
    

    elif choice == 2:
        """get the data for 2D array"""
        rows = int(input("Enter Data for a 2D array rows: "))
        cols = int(input("Enter Data for a 2D array cols: "))
        

        for x in range(rows):
            l=[]
            for i in range(cols):
                num = int (input("enter the number "))
                l.append(num)
            data.append(l)

    
    print("Successfully data input for 2D array: ")

def converter(data):
    
    if len(data)>0 and isinstance(data[0],list):
        l=[]
        for i in data:
            l.extend(i)
        return l
    else:
        return data 

def data_summary():
        """Display Data Summary of The Dataset Using Built-in functions."""

        l = converter(data)
   
        print("Data Summary")
        print(f"Total Value :- {len(l)}")
        print(f"Minimum Value :- {min(l)}")
        print(f"Maximum Value :- {max(l)}")
        print(f"Sum of all Value :- {sum(l)}")
        print(f"Average Value :- {sum(l) / len(l)}")

def fact(n):
    
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def factorial():
    """Calculate factorial of a number using recursion"""

    num = int(input("Enter your factorial number: "))

    if num <0:
        print("Factorial is not possible!")

    else:
        result = fact(num)
        print(f"Factorial of {num} is: {result}")

def threshold_data(): 
    l = converter(data)
    """Filter data based on a threshold values using a lambda function"""   
    thr=int(input("Enter a threshold value to filter out data above this value:"))
    x = filter(lambda a: a > thr , l)
    print(f"Data filtered by threshold (value >={thr}):")
    print(*x,sep=" , ")

def sort_data():
    """Sorting the data in ascending or descending order."""

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
        
    choice = int(input("Enter your choice number: "))
        
    if choice == 1:
        sorted_data = sorted(data)
        

        print("Sorted Data in Ascending Order:")
        print(sorted_data)
        
    

    elif choice == 2:
        sorted_data = sorted(data, reverse=True)

        print("Sorted Data in Descending Order:")
        print(sorted_data)

    else:
        print("Invalid sorting choice")

def dataset_statistics():
    """Display dataset statistics using the dataset_statistics function."""
    
    print("Dataset Statistics:")
    minimum = min(l)
    maximum = max(l)
    total  = sum(l)
    average = sum(l) / len(l)

    return minimum,maximum,total,average

while True:
    print()
    print("Main Menu: ")
    print()
    print("1. InputData")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. sort Data")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


    choice = int(input("Please enter your choice number : "))

    if choice == 1:
        print(input_data.__doc__) 
        input_data()

    elif choice == 2:
        print(data_summary.__doc__)
        data_summary() 

    elif choice == 3:
        print(factorial.__doc__)
        factorial()

    elif choice == 4:
        print(threshold_data.__doc__)
        threshold_data()

    elif choice == 5:
        print(sort_data.__doc__)
        sort_data()
            
    elif choice == 6:
         print(dataset_statistics.__doc__)
         l = converter(data)
         minimum,maximum,total,average = dataset_statistics()
         print(f"Minimum Value: {minimum}")
         print(f"Maximum Value: {maximum}")
         print(f"Sum of all values: {total}")
         print(f"Average Value: {average}")
          
         
    
    elif choice == 7:
        print("Exiting the program: ")
        break
    else:
        print("Invalid choice number please try again:")

          

    
     