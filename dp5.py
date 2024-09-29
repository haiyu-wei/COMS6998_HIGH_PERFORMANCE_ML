import numpy as np
import time
import argparse

from numpy.core.multiarray import result_type


# Main function to handle argument parsing and computation
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="NumPy dot product performance test.")
    parser.add_argument('--N', type=int, default=1000000, help="Size of the vectors")
    parser.add_argument('--repetitions', type=int, default=1000, help="Number of repetitions")

    args = parser.parse_args()

    N = args.N  # Size of the vectors
    repetitions = args.repetitions  # Number of repetitions

    # Initialize arrays with ones, dtype=float32
    A = np.ones(N, dtype=np.float32)/3
    B = np.ones(N, dtype=np.float32)/3

    # Timing NumPy's built-in dot product for the second half of repetitions
    start_time = time.time()
    result = 0
    for i in range(repetitions // 2, repetitions):  # Timing the second half of the repetitions
        result = np.dot(A, B)
    end_time = time.time()

    print(result)
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