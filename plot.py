import numpy as np
import matplotlib.pyplot as plt

# Constants for the roofline model
peak_flops = 200  # GFLOPS
memory_bandwidth = 30  # GB/s

# # Arithmetic intensities and performance measurements from the data in the images
# arithmetic_intensities = np.array([0.000000265, 0.000000257, 0.000000256, 0.000000290, 0.0000369910,
#                                    0.0286548357, 0.042753, 0.0187896, 0.0014135, 0.042753])
#
# performance = np.array([90566037.735849, 311284.046693, 312989.045383, 8275862.068966, 54067141224.778648,
#                         83.755497, 1068466.502, 10644602.024627, 56.766402, 10688238.148258])

# Provided Bandwidth (B) in GB/sec and Performance (P) in FLOP/sec for each case
bandwidth = np.array([
    311284.046693, 90566037.735849, 312989.045383, 8275862.068966, 216.268565,
    83.755497, 0.042578, 0.042753, 55.766420, 30.190025
])

performance_flops = np.array([
    77821011673152.281250, 22641509433962264.000000, 312989045383413.687500,
    8275862068965518.000000, 54067141224.778648, 20938874201.955376,
    10644602.024627, 10688238.148258, 13941605063.021858, 7547506345.366061
])

# Calculate Arithmetic Intensity (AI) in FLOPs per byte
arithmetic_intensity = performance_flops / (bandwidth * 1e9)  # Convert GB to bytes
# Generate x-values for the roofline plot
intensity_range = np.logspace(-2, 2)

# Roofline equation: Performance = min(peak_flops, memory_bandwidth * arithmetic_intensity)
roofline = np.minimum(peak_flops, memory_bandwidth * intensity_range)

# Optimizing the plot to better show the relationship between arithmetic intensity and performance

plt.figure(figsize=(10, 7))

# Plot the roofline
plt.loglog(intensity_range, roofline, label="Roofline", color="red", linewidth=2)

# Plot the benchmark points with clearer size and colors for distinction
plt.scatter(arithmetic_intensity, performance_flops / 1e9, color="blue", s=100, edgecolor="black", label="Microbenchmark Data", zorder=5)

# Add labels and titles with larger font sizes for clarity
plt.title("Roofline Model with Microbenchmark Data", fontsize=16)
plt.xlabel("Arithmetic Intensity (FLOPs/Byte)", fontsize=14)
plt.ylabel("Performance (GFLOPs)", fontsize=14)

# Adjust grid visibility and style
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.axvline(x=np.mean(arithmetic_intensity), color='green', linestyle='--', label='Average Arithmetic Intensity')

# Adjust tick labels size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add a legend with a slightly larger size
plt.legend(fontsize=12)

# Show the plot with adjusted layout
plt.tight_layout()
plt.show()