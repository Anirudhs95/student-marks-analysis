# Student Marks Analysis System
import csv
import numpy as np

names = []
mark = []

with open("student-marks-analysis/students.csv") as student:
    data = csv.DictReader(student)
    for row in data:
        names.append(row['Name'])
        mark.append(row['Marks'])

marks = np.array((mark),dtype='int32')

def marks_avg(data):
    return np.average(data)


def find_topper(arr, names):
    max_marks = np.max(arr)
    index = arr.tolist().index(max_marks)
    return names[index], max_marks

average = marks_avg(marks)
topper_name, topper_marks = find_topper(marks, names)

print("Average Marks:", average)
print("Topper:", topper_name)
print("Topper Marks:", topper_marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

with open("student-marks-analysis/summary.csv",'w',newline="") as file:
    write = csv.writer(file)
    write.writerow(["Metric", "Value"])
    write.writerow(["Average Marks", average])
    write.writerow(["Topper", topper_name])
    write.writerow(["Topper Marks", topper_marks])
