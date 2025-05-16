#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
fruit_names = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Positions of bars on x-axis
x = np.arange(len(people))

# Initialize the bottom array for stacking
bottom = np.zeros(len(people))

plt.figure(figsize=(8,6))

# Plot each fruit stacked
for i in range(fruit.shape[0]):
    plt.bar(x, fruit[i], bottom=bottom, color=colors[i], width=0.5, label=fruit_names[i])
    bottom += fruit[i]  # Update bottom to stack the next fruit on top

plt.xticks(x, people)
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
