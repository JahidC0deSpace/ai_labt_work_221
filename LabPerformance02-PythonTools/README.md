# LabPerformance02-PythonTools

This Python script performs various operations, including removing duplicates from a list, finding common elements between two lists, sorting student data, counting word occurrences, generating and analyzing matrices, normalizing arrays, processing sales data, and visualizing data using Matplotlib.

---

## 1. Remove Duplicates and Sort a List

### Input:
- The user is prompted to enter the number of elements in the list.
- The user then inputs the elements one by one.
- Enter number of elements: 5
- 10 20 10 30 20

### Output:
- Sorted list without duplicates: [10, 20, 30]

---

## 2. Find Common Elements Between Two Lists

### Input:
- The user inputs two lists of numbers separated by spaces.
- Enter numbers for first list: 1 2 3 4
- Enter numbers for second list: 3 4 5 6

### Output:
- Common elements: [3, 4]

---

## 3. Sort Students by Grade

### Input:
- Enter the number of students: 6 
- Enter name of student 1: Mim 
- Enter age of student 1: 20 
- Enter grade of student 1: 88 
- Enter name of student 2: Samir 
- Enter age of student 2: 22 
- Enter grade of student 2: 78 
- Enter name of student 3: Jahid 
- Enter age of student 3: 21 
- Enter grade of student 3: 85 
- Enter name of student 4: Jitu 
- Enter age of student 4: 24 
- Enter grade of student 4: 70 
- Enter name of student 5: Ismu 
- Enter age of student 5: 20 
- Enter grade of student 5: 90 
- Enter name of student 6: Rakib 
- Enter age of student 6: 23 
- Enter grade of student 6: 44

### Output:
- Students sorted by grade: ('Rakib', 23, 44) ('Jitu', 24, 70) ('Samir', 22, 78) ('Jahid', 21, 85) ('Mim', 20, 88) ('Ismu', 20, 90)


---

## 4. Count Word Occurrences in a Text

### Input:
- Enter a text: Hello world! Hello everyone.

### Output:
- Word occurrences:
- hello: 2
- world: 1
- everyone: 1


---

## 5. Generate and Analyze a 5x5 Matrix

### Input:
- Generated 5x5 Matrix:
- [[12 34 56 78 90]
- [23 45 67 89 10]
- [11 22 33 44 55]
- [66 77 88 99 00]
- [21 32 43 54 65]]

### Output:
- Row-wise Sums: [270 234 165 330 215]


---

## 6. Normalize an Array

### Input:
- Original Array:
- [70.3646129 53.80752911 38.55451698 18.19494994 37.96132758...]

### Output:
- Normalized Array:
- [0.70401397 0.53731818 0.3837517 0.17877272...] 

### Example:


---

## 7. Process Sales Data

### Input:
- A CSV file (`sales_data.csv`) containing columns: `Product`, `Quantity`, and `Price`.
- Product,Quantity,Price
- Laptop,5,700
- Phone,10,300
- Laptop,3,700
- Tablet,8,250
- Phone,7,300

### Output:
- Total Revenue per Product:
- Laptop: 5600
- Phone: 5100
- Tablet: 2000


---

## 8. Handle Missing Data in a CSV File

### Input:
- A CSV file (`missing_data.csv`) with missing values.
- Dataset before filling missing values:
- ID Name Age Salary
- 1 Alice 25.0 50000.0
- 2 Bob NaN 60000.0
- 3 Carol 30.0 NaN
- 4 Dave 28.0 55000.0

### Output:
- Dataset after filling missing values:
- ID Name Age Salary
- 1 Alice 25.000000 50000.0
- 2 Bob 27.666667 60000.0
- 3 Carol 30.000000 55000.0
- 4 Dave 28.000000 55000.0




---

## 9. Visualize Temperature Data

### Input:
- days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
- temperatures = [22, 24, 20, 26, 23, 25, 21] 

### Output:
- A line plot showing the temperature trend over the week.


---

## 10. Visualize Sales Revenue by Region

### Input:
- regions = ["North", "South", "East", "West", "Central"]
- sales_revenue = [50000, 70000, 65000, 80000, 72000] 

### Output:
- A bar chart comparing sales revenue across regions.


---

## How to Run the Code

1. Ensure you have Python installed.
2. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib