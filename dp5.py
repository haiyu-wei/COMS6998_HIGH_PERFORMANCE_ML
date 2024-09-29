import numpy as np
import time
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="NumPy dot product performance test.")
    parser.add_argument('--N', type=int, default=1000000)
    parser.add_argument('--repetitions', type=int, default=1000)

    args = parser.parse_args()

    N = args.N
    repetitions = args.repetitions

    # Initialize arrays with 1/3
    A = np.ones(N, dtype=np.float32)/3
    B = np.ones(N, dtype=np.float32)/3

    start_time = time.time()
    result = 0
    for i in range(repetitions // 2, repetitions):  # Timing the second half of the repetitions
        result = np.dot(A, B)
    end_time = time.time()

    print(result)
    # Calculate the average time for the second half of repetitions
    average_time = (end_time - start_time) / (repetitions // 2)

    bytes_accessed = 2 * N * 4  # 2 arrays, N elements each, 4 bytes per float32
    bandwidth = (bytes_accessed / 1e9) / average_time  # Convert to GB/sec

    # Calculate FLOP/sec
    flops = (2 * N) / average_time  # 2 operations

    print(f"N: {N} <T>: {average_time:.6f} sec B: {bandwidth:.6f} GB/sec F: {flops:.6f} FLOP/sec")

if __name__ == "__main__":
    main()