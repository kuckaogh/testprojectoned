/*
 * Copyright 1993-2009 NVIDIA Corporation.  All rights reserved.
 *
 * NVIDIA Corporation and its licensors retain all intellectual property and 
 * proprietary rights in and to this software and related documentation. 
 * Any use, reproduction, disclosure, or distribution of this software 
 * and related documentation without an express license agreement from
 * NVIDIA Corporation is strictly prohibited.
 *
 * Please refer to the applicable NVIDIA end user license agreement (EULA) 
 * associated with this source code for terms and conditions that govern 
 * your use of this NVIDIA software.
 * 
 */

/* Example of integrating CUDA functions into an existing 
 * application / framework.
 * Host part of the device code.
 * Compiled with Cuda compiler.
 */

// includes, system
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// includes, project
#include <cutil_inline.h>
//#include <shrUtils.h>
// includes, kernels
#include <cppIntegration_kernel.cu>
//
////////////////////////////////////////////////////////////////////////////////
// declaration, forward

extern "C" void
computeGold(char* reference, char* idata, const unsigned int len);
extern "C" void
computeGold2(int2* reference, int2* idata, const unsigned int len);

////////////////////////////////////////////////////////////////////////////////
//! Entry point for Cuda functionality on host side
//! @param argc  command line argument count
//! @param argv  command line arguments
//! @param data  data to process on the device
//! @param len   len of \a data
////////////////////////////////////////////////////////////////////////////////
extern "C" void
runTest(const int argc, const char** argv, char* data, int2* data_int2, unsigned int len, float* h_C)
{

    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    if( cutCheckCmdLineFlag(argc, (const char**)argv, "device") )
        cutilDeviceInit(argc, (char**)argv);
    else
        cudaSetDevice( cutGetMaxGflopsDeviceId() );

    const unsigned int num_threads = len / 4;
    cutilCondition(0 == (len % 4));
    const unsigned int mem_size = sizeof(char) * len;
    const unsigned int mem_size_int2 = sizeof(int2) * len;

    // allocate device memory
    char* d_data;
    cutilSafeCall(cudaMalloc((void**) &d_data, mem_size));
    // copy host memory to device
    cutilSafeCall(cudaMemcpy(d_data, data, mem_size,
                            cudaMemcpyHostToDevice) );
    // allocate device memory for int2 version
    int2* d_data_int2;
    cutilSafeCall(cudaMalloc((void**) &d_data_int2, mem_size_int2));
    // copy host memory to device
    cutilSafeCall(cudaMemcpy(d_data_int2, data_int2, mem_size_int2,
                            cudaMemcpyHostToDevice) );

    // setup execution parameters
    dim3 grid(1, 1, 1);
    dim3 threads(num_threads, 1, 1);
    dim3 threads2(len, 1, 1); // more threads needed fir separate int2 version
    // execute the kernel
    kernel<<< grid, threads >>>((int*) d_data);
    kernel2<<< grid, threads2 >>>(d_data_int2);


    // check if kernel execution generated and error
    cutilCheckMsg("Kernel execution failed");

    // compute reference solutions
    char* reference = (char*) malloc(mem_size);
    computeGold(reference, data, len);
    int2* reference2 = (int2*) malloc(mem_size_int2);
    computeGold2(reference2, data_int2, len);

    // copy results from device to host
    cutilSafeCall(cudaMemcpy(data, d_data, mem_size,
                            cudaMemcpyDeviceToHost));
    cutilSafeCall(cudaMemcpy(data_int2, d_data_int2, mem_size_int2,
                            cudaMemcpyDeviceToHost));

    // check result
    bool success = true;
    for(unsigned int i = 0; i < len; i++ )
    {
        if( reference[i] != data[i] || 
	    reference2[i].x != data_int2[i].x || 
	    reference2[i].y != data_int2[i].y)
            success = false;
    }
    printf("Test %s\n", success ? "PASSED" : "FAILED");

    // cleanup memory
    cutilSafeCall(cudaFree(d_data));
    cutilSafeCall(cudaFree(d_data_int2));
    free(reference);
    free(reference2);

	int N=10;
    size_t  size = N * sizeof(float);
	float* d_A;
	cudaMalloc((void**)&d_A, size);
	float* d_B;
	cudaMalloc((void**)&d_B, size);
	float* d_C;
	cudaMalloc((void**)&d_C, size);
    float h_A_v =3.0;
	float h_B_v =4.0;
	//float h_C_v =0;

	float* h_A;
	float* h_B;
//	float* h_C;
	h_A = &h_A_v;
	h_B = &h_B_v;
	//h_C = &h_C_v;

	cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

	// Invoke kernel
	int threadsPerBlock = 256;
//	int blocksPerGrid =	(N + threadsPerBlock � 1) / threadsPerBlock;
	simpleAdd<<<1, N>>>(d_A, d_B, d_C);
	// Copy result from device memory to host memory
	// h_C contains the result in host memory
	cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
	// Free device memory
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);

    cudaThreadExit();
}