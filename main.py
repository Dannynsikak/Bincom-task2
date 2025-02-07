import os
import re

# question 1: write and read full name 
file_name = "name.txt"

# step 1 create and write the full name to the text file 
with open(file_name, "w") as file:
    file.write("Ofonime Nsikak Eno")

# step 2 read and extract name parts
with open(file_name, "r")as file:
    full_name = file.read().strip()

name_parts = full_name.split()

first_name = name_parts[0]
surname = name_parts[1] if len(name_parts) > 2 else ""
last_name = name_parts[-1]

print(f"First Name: {first_name}")
print(f"Surname: {surname}")
print(f"Last Name: {last_name}")

# Question 2: print local file path
local_path = os.path.abspath(file_name)
print(f"Local Path: {local_path}")

# Question 3: extract baby names from HTML using Regex 
html_data = """
<h3 align="center">Popularity in 2020</h3>
<table summary="...">
<tr align="right"><td>1</td><td>Olivia</td><td>Liam</td></tr>
<tr align="right"><td>2</td><td>Emma</td><td>Noah</td></tr>
<tr align="right"><td>3</td><td>Ava</td><td>Oliver</td></tr>
</table>
"""

# using regex to extract baby names 
pattern = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
matches = re.findall(pattern, html_data)

baby_names = []
for rank, girl_name, boy_name in matches:
    baby_names.append((int(rank), girl_name, boy_name))

# sorting names by gender
baby_names.sort()

print("\nExracted Baby Names:")
for rank, girl, boy in baby_names:
    print(f"Rank: {rank}: {girl}, {boy}")

# Question 4: Sorting Algorithm (Bubble Sort) and Binary Search
def bubble_sort(arr):
    """Sorts an array using Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    """Implements binary search to find an element in a sorted list."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example list and target
numbers = [34, 7, 23, 32, 5, 62]
sorted_numbers = bubble_sort(numbers)
print("\nSorted Numbers:", sorted_numbers)

target_number = 23
index = binary_search(sorted_numbers, target_number)
if index != -1:
    print(f"Binary Search: {target_number} found at index {index}")
else:
    print(f"Binary Search: {target_number} not found")