import numpy as np
import matplotlib.pyplot as plt

# Example task times (randomised)
mean_time = 40
std_dev = 5
n = 5000

# Simulate project completion times
completion_times = np.random.normal(mean_time, std_dev, n)

deadlines = [30, 40, 45]

plt.hist(completion_times, bins=30, color='skyblue', edgecolor='black')
for d in deadlines:
    plt.axvline(d, color='red', linestyle='--', label=f"Deadline {d} days")

plt.title("Monte Carlo Risk Assessment: Completion Time Distribution")
plt.xlabel("Completion Time (days)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

for d in deadlines:
    prob = np.mean(completion_times <= d)
    print(f"Probability of finishing before {d} days: {prob:.4f}")