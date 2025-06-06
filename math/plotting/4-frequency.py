#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
student_grades = np.clip(student_grades, 0, 100)
bins = np.arange(0, 101, 10)
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
plt.hist(student_grades, bins=bins, edgecolor='black')
plt.show()