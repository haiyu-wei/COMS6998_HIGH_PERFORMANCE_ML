#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Dot product function
float dp(long N, float *pA, float *pB) {
    float R = 0.0;

    for (long j = 0; j < N; j++) {
        R += pA[j] * pB[j];
    }
    return R;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <vector_size> <repetitions>\n", argv[0]);
        return -1;
    }

    long N = atol(argv[1]);
    int repetitions = atoi(argv[2]);

    float *pA = (float *)malloc(N * sizeof(float));
    float *pB = (float *)malloc(N * sizeof(float));

    for (long i = 0; i < N; i++) {
        pA[i] = 1.0;
        pB[i] = 1.0;
    }

    struct timespec start, end;
    double total_time = 0.0;


    for (int j = 0; j < repetitions; j++) {
        clock_gettime(CLOCK_MONOTONIC, &start);
        dp(N, pA, pB);
        clock_gettime(CLOCK_MONOTONIC, &end);

        double time_spent = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

        if (j >= repetitions / 2) {
            total_time += time_spent;
        }
    }

    double average_time = total_time / (repetitions / 2);


    double bytes_accessed = 2.0 * N * sizeof(float);
    double bandwidth = (bytes_accessed / 1e9) / average_time;

    // Calculate FLOP/sec
    double flops = (8.0 * N) / average_time;

    // Print the results
    printf("N: %ld <T>: %.10f sec B: %.6f GB/sec F: %.6f FLOP/sec\n", N, average_time, bandwidth, flops);

    // Free memory
    free(pA);
    free(pB);

    return 0;
}