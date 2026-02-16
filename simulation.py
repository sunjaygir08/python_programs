import numpy as np
import matplotlib.pyplot as plt

# Generate 10,000 random numbers (Uniform distribution)
random_uniform_large = np.random.rand(10000)

# Plot histogram with 50 bins
plt.figure(figsize=(7, 5))
plt.hist(random_uniform_large, bins=50, color='skyblue', edgecolor='black')
plt.title('Histogram of 10,000 Uniform Random Numbers')
plt.xlabel('Value') 
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)  
plt.show()
