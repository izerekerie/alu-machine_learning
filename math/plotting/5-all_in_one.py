#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Set up flexible layout: 3 rows x 2 columns
fig = plt.figure(figsize=(12, 12))
gs = gridspec.GridSpec(3, 2, figure=fig)

# --- Plot 1: y = x^3 ---
ax1 = fig.add_subplot(gs[0, 0])
x = np.arange(0, 11)
y = x ** 3
ax1.plot(x, y, color='red')
ax1.set_xlim(0, 10)
ax1.set_title('y = x³')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)

# --- Plot 2: Height vs Weight Scatter ---
ax2 = fig.add_subplot(gs[0, 1])
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x2, y2 = np.random.multivariate_normal(mean, cov, 2000).T
y2 += 180
ax2.scatter(x2, y2, c='magenta', s=10)
ax2.set_xlim(0, 150)
ax2.set_ylim(0, 250)
ax2.set_title("Men's Height vs Weight")
ax2.set_xlabel('Height (in)')
ax2.set_ylabel('Weight (lbs)')

# --- Plot 3: Exponential Decay (C-14 log scale) ---
ax3 = fig.add_subplot(gs[1, 0])
x3 = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y3 = np.exp((r / t) * x3)
ax3.plot(x3, y3)
ax3.set_xlim(0, 28650)
ax3.set_yscale('log')
ax3.set_title('Exponential Decay of C-14')
ax3.set_xlabel('Time (years)')
ax3.set_ylabel('Fraction Remaining')

# --- Plot 4: Dual Decay Plot ---
ax4 = fig.add_subplot(gs[1, 1])
x4 = np.arange(0, 21000, 1000)
t1 = 5730
t2 = 1600
y4_1 = np.exp((r / t1) * x4)
y4_2 = np.exp((r / t2) * x4)
ax4.plot(x4, y4_1, label='C-14', color='red', linestyle='--')
ax4.plot(x4, y4_2, label='Ra-226', color='green')
ax4.set_xlim(0, 21000)
ax4.set_ylim(0, 1)
ax4.set_title('Exponential Decay of Radioactive Elements')
ax4.set_xlabel('Time (years)')
ax4.set_ylabel('Fraction Remaining')
ax4.legend()

# --- Plot 5: Histogram (spanning full width) ---
ax5 = fig.add_subplot(gs[2, :])  # Span both columns
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
student_grades = np.clip(student_grades, 0, 100)
bins = np.arange(0, 101, 10)
ax5.hist(student_grades, bins=bins, edgecolor='black')
ax5.set_xlim(0, 100)
ax5.set_ylim(0, 30)
ax5.set_title('Project A')
ax5.set_xlabel('Grades')
ax5.set_ylabel('Number of Students')

# Adjust layout
plt.tight_layout()
plt.show()
