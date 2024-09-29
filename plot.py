# Importing necessary libraries again
import numpy as np
import matplotlib.pyplot as plt

# Constants for the roofline model
peak_flops = 200  # GFLOPS
memory_bandwidth = 30  # GB/s

# Bandwidth (B) in GB/sec and Performance (P) in FLOP/sec for each case
bandwidth = np.array([
    8.559552, 8.471530, 30.945870, 21.037585, 209.888366,
    70.991004, 0.042578, 0.042753, 55.766420, 30.190025
])

performance_flops = np.array([
    2139888069.559509, 2117882603.746814, 30945870033.426727, 21037585147.423515, 52472091406.383240,
    17747751107.029285, 10644602.024627, 10688238.148258, 13941605063.021858, 7547506345.366061
])

# Calculate Arithmetic Intensity (AI) in FLOPs per byte
arithmetic_intensity = performance_flops / (bandwidth * 1e9)  # Convert GB to bytes

# Generate x-values for the roofline plot
intensity_range = np.logspace(-2, 2, 100)

# Roofline equation: Performance = min(peak_flops, memory_bandwidth * intensity)
roofline = np.minimum(peak_flops, memory_bandwidth * intensity_range)

# Optimizing the plot to better show the relationship between arithmetic intensity and performance
plt.figure(figsize=(10, 7))

# Plot the roofline
plt.loglog(intensity_range, roofline, label="Roofline", color="red", linewidth=2)

# Plot the benchmark points for dp1 (data points 1 and 2)
plt.scatter(arithmetic_intensity[0:2], performance_flops[0:2] / 1e9, color="blue", s=100, edgecolor="black", label="dp1", zorder=5)
plt.scatter(arithmetic_intensity[2:4], performance_flops[2:4] / 1e9, color="green", s=100, edgecolor="black", label="dp2", zorder=5)
plt.scatter(arithmetic_intensity[4:6], performance_flops[4:6] / 1e9, color="orange", s=100, edgecolor="black", label="dp3", zorder=5)
plt.scatter(arithmetic_intensity[6:8], performance_flops[6:8] / 1e9, color="purple", s=100, edgecolor="black", label="dp4", zorder=5)
plt.scatter(arithmetic_intensity[8:], performance_flops[8:] / 1e9, color="yellow", s=100, edgecolor="black", label="dp5", zorder=5)


# Add labels and titles with larger font sizes for clarity
plt.title("Roofline Model with Microbenchmark Data", fontsize=16)
plt.xlabel("Arithmetic Intensity (FLOPs/Byte)", fontsize=14)
plt.ylabel("Performance (GFLOPs)", fontsize=14)

# Adjust grid visibility and style
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Plot the vertical line where peak performance intersects with memory-bound slope
plt.axvline(x=peak_flops / memory_bandwidth, color='green', linestyle='--', label='Intersection at AI = 6.67')

# Adjust tick labels size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add a legend with a slightly larger size
plt.legend(fontsize=12)

# Show the plot with adjusted layout
plt.tight_layout()
plt.show()