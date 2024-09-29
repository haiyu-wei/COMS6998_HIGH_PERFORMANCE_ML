#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <mkl_cblas.h>


float bdp(long N, float *pA, float *pB) {
    float R = cblas_sdot(N, pA, 1, pB, 1);
    return R;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <vector_size> <repetitions>\n", argv[0]);
        return -1;
    }

    long N = atol(argv[1]);
    int repetitions = atoi(argv[2]);

    // allocate memory for two arrays
    float *pA = (float *)malloc(N * sizeof(float));
    float *pB = (float *)malloc(N * sizeof(float));

    // initialize arrays
    for (long i = 0; i < N; i++) {
        pA[i] = 1.0;
        pB[i] = 1.0;
    }

    struct timespec start, end;
    double total_time = 0.0;

    float result = 0.0;
    for (int j = 0; j < repetitions; j++) {
        // only calculate the time spent on dp function
        clock_gettime(CLOCK_MONOTONIC, &start);
        // need to use the result, otherwise it will be passed by compiler
        result += bdp(N, pA, pB);
        clock_gettime(CLOCK_MONOTONIC, &end);

        double time_spent = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

        // only calculate the second half of the repetitions
        if (j >= repetitions / 2) {
            total_time += time_spent;
        }
    }

    printf("Result: %f\n", result);

    double average_time = total_time / (repetitions / 2);


    double bytes_accessed = 2.0 * N * sizeof(float);
    double bandwidth = (bytes_accessed / 1e9) / average_time;

    // Calculate FLOP/sec
    double flops = (2.0 * N) / average_time;

    // Print the results
    printf("N: %ld <T>: %.10f sec B: %.6f GB/sec F: %.6f FLOP/sec\n", N, average_time, bandwidth, flops);

    // Free memory
    free(pA);
    free(pB);

    return 0;
}
