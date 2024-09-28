import numpy as np
import time
import argparse

# Function to compute dot product using a simple loop
def dp(N, A, B):
    R = 0.0
    for j in range(N):
        R += A[j] * B[j]
    return R

# Main function to handle argument parsing and computation
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Dot product performance test.")
    parser.add_argument('--N', type=int, default=300000000, help="Size of the vectors")
    parser.add_argument('--repetitions', type=int, default=20, help="Number of repetitions")

    args = parser.parse_args()

    N = args.N  # Size of the vectors
    repetitions = args.repetitions  # Number of repetitions

    # Initialize arrays with ones, dtype=float32
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)

    # Timing the function for the second half of repetitions
    start_time = time.time()
    for i in range(repetitions // 2, repetitions):  # Timing the second half of the repetitions
        result = dp(N, A, B)
    end_time = time.time()

    # Calculate the average time for the second half of repetitions
    average_time = (end_time - start_time) / (repetitions // 2)

    # Calculate bandwidth in GB/sec
    bytes_accessed = 2 * N * 4  # 2 arrays, N elements each, 4 bytes per float32
    bandwidth = (bytes_accessed / 1e9) / average_time  # Convert to GB/sec

    # Calculate FLOP/sec
    flops = (2 * N) / average_time  # 2 operations (multiply and add) per element

    # Print the results in the required format
    print(f"N: {N} <T>: {average_time:.6f} sec B: {bandwidth:.6f} GB/sec F: {flops:.6f} FLOP/sec")

if __name__ == "__main__":
    main()