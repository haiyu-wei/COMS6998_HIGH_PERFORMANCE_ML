import numpy as np
import time
import argparse


def dp(N, A, B):
    R = 0.0
    for j in range(N):
        R += A[j] * B[j]
    return R

def main():
    parser = argparse.ArgumentParser(description="Dot product performance test.")
    parser.add_argument('--N', type=int, default=300000000)
    parser.add_argument('--repetitions', type=int, default=20)

    args = parser.parse_args()

    N = args.N
    repetitions = args.repetitions

    # Initialize arrays with 1/3
    result = 0
    A = np.ones(N, dtype=np.float32)/3
    B = np.ones(N, dtype=np.float32)/3

    start_time = time.time()
    for i in range(repetitions // 2, repetitions):  # Timing the second half of the repetitions
        result = dp(N, A, B)
    end_time = time.time()

    print(result)

    # Calculate the average time for the second half of repetitions
    average_time = (end_time - start_time) / (repetitions // 2)

    # Calculate bandwidth in GB/sec
    bytes_accessed = 2 * N * 4  # 2 arrays, N elements each, 4 bytes per float32
    bandwidth = (bytes_accessed / 1e9) / average_time  # Convert to GB/sec

    # Calculate FLOP/sec
    flops = (2 * N) / average_time  # 2 operations

    # Print the results in the required format
    print(f"N: {N} <T>: {average_time:.6f} sec B: {bandwidth:.6f} GB/sec F: {flops:.6f} FLOP/sec")

if __name__ == "__main__":
    main()