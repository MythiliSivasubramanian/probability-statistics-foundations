"""
Task 01 — Measures of Central Tendency (Mean)

Problem:Analyze the number of daily website visitors for a startup over 7 days.
Dataset: visitors = [120, 150, 130, 170, 160, 180, 140]

Tasks:
1. Calculate the Mean of visitors.
2. Observe what happens to the mean if the 7th day had 1000 visitors instead of 140. (outliners)


Key Insight
-----------
Mean is sensitive to outliers.
A single extreme value can heavily shift the average and misrepresent the dataset.
"""

# Original dataset: Daily visitors for 7 days
visitors = [120, 150, 130, 170, 160, 180, 140]
print("\n\nOriginal dataset: Daily visitors for 7 days : \n",visitors)

# Calculate mean using sum and length. Mean = Sum of all observations / Number of observations
visitors_mean = sum(visitors) / len(visitors)
print("Mean (Average visitors per day):", visitors_mean)

# Scenario: Outlier introduced. 7th day visitors changed from 140 → 1000
visitors_new_data = [120, 150, 130, 170, 160, 180, 1000]

# Mean is sensitive to outliers.
# A single extreme value can heavily shift the average.
visitors_new_mean = sum(visitors_new_data) / len(visitors_new_data)

print("\nMean with outlier (1000 visitors on day 7):",
      round(visitors_new_mean, 2))


# Interpretations
print("\nInsight:")
print("The mean increased drastically from", round(visitors_mean,2),"to", round(visitors_new_mean,2), "due to one extreme value 1000.")
print("This shows that mean alone may not represent typical behavior.")

# Additional Examples
data_normal = [10, 12, 11, 13, 12]
data_outlier = [10, 12, 11, 13, 100]

print("\nNormal_data :",data_normal)
print("Mean (normal):", sum(data_normal)/len(data_normal))

print("\n\nData with an Outlier '100':", data_outlier)
print("Mean (with outlier):", sum(data_outlier)/len(data_outlier),"\n\n")

# Median for Odd no of values
# Dataset Marks with odd no of values
marks = [72, 65, 78, 90, 85, 60, 88] 

# Find median.
sorted_marks = sorted(marks)
print("\n\nSorted marks :\n",sorted_marks)
count = len(sorted_marks) # len = 7 (odd number)

# Median is the middle value after sorting.
mid = count // 2 # integer index of middle element (works for odd no of values)
median_value_odd = sorted_marks[mid]
print("\nMedian(odd no of values) :",median_value_odd)

# Median for even no of values
# Dataset temperatures with even no of values
temperatures = [22, 24, 19, 21, 23, 20]
sorted_temp = sorted(temperatures)
print("\n\nSorted temperatures :\n", sorted_temp)

count_temp = len(sorted_temp) # len = 6 (even number)

if count_temp % 2 != 0: # Odd number of values
    mid_value = count_temp // 2
    median_tem = sorted_temp[mid_value]
    
else: # Even no of values - Avg(two middle values)
    
    # Middle 2 indicies
    mid_1 = (count_temp // 2 ) - 1
    mid_2 = count_temp // 2
  
    # Average of middle VALUES (not indices)
    median_tem = (
        sorted_temp[mid_1] +
        sorted_temp[mid_2]
    ) / 2

print("\nMiddle values:", sorted_temp[mid_1], ",",sorted_temp[mid_2])

print("\nMedian (even no. of values):", median_tem)