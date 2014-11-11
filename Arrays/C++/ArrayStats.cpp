/*
 * =====================================================================================
 *
 *       Filename:  ArrayStats.cpp
 *
 *    Description:  Contains functions to find statistics of an array
 *					like maximum, minimum, or std deviation
 *
 *        Version:  1.0
 *        Created:  11/07/2014 11:15:51 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Phillip (), philliplemons512@gmail.com
 *   Organization:
 *
 * =====================================================================================
 */

#include <stdexcept>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <math.h>

template<typename T>
void PrintArray(T arr[], int n)
{
	std::string prefix = "[ ";
	for (int i = 0; i < n; i++)
	{
		std::cout << prefix << arr[i];
		prefix = ", ";
	}
	std::cout << " ]" << std::endl;
}

template<typename T>
T findMinimum(T arr[], int n)
{
	if (n == 0)
	{
		throw std::length_error("Can't find min of zero-length array");
	}

	T min = arr[0];
	for (int i = 0; i < n; i++)
	{
		if (arr[i] < min)
		{
			min = arr[i];
		}
	}
	return min;
}

template<typename T>
T findMaximum(T arr[], int n)
{
	if (n == 0)
	{
		throw std::length_error("Can't find max of zero-length array");
	}

	T max = arr[0];
	for (int i = 0; i < n; i++)
	{
		if (arr[i] > max)
		{
			max = arr[i];
		}
	}
	return max;
}

template<typename T>
T findAverage(T arr[], int n)
{
	T total = 0;
	for (int i = 0; i < n; i++)
	{
		total += arr[i];
	}

	return total/n;
}

template<typename T>
double findSampleVariance(T arr[], int n)
{
	T average = findAverage(arr, n);

	double arr_sum = 0;
	for (int i = 0; i < n; i++)
	{
        arr_sum += pow((arr[i] - average), 2);
	}

	return arr_sum / n;
}

template<typename T>
double findStdDeviation(T arr[], int n)
{
	double sampleVariance = findSampleVariance(arr, n);

	return sqrt(sampleVariance);
}

int main ( int argc, char *argv[] )
{
	int arr[] = {1,2,3,4,6,7,0};
	PrintArray(arr, 7);
	std::cout << "Minimum: " << findMinimum(arr, 7) << std::endl;
	std::cout << "Maximum: " << findMaximum(arr, 7) << std::endl;
	std::cout << "Average: " << findAverage(arr, 7) << std::endl;
	std::cout << "Sample Variance: " << findSampleVariance(arr, 7) << std::endl;
	std::cout << "Standard Deviation: " << findStdDeviation(arr, 7) << std::endl;
	std::cout << std::endl;

	double arr2[] = { 6.4, 2.0, 3.7, 4.1, 6.6, 7.3, 49.7 };
	PrintArray(arr2, 7);
	std::cout << "Minimum: " << findMinimum(arr2, 7) << std::endl;
	std::cout << "Maximum: " << findMaximum(arr2, 7) << std::endl;
	std::cout << "Average: " << findAverage(arr2, 7) << std::endl;
	std::cout << "Sample Variance: " << findSampleVariance(arr2, 7) << std::endl;
	std::cout << "Standard Deviation: " << findStdDeviation(arr2, 7) << std::endl;
	std::cout << std::endl;

	std::string arr3[] = {"hello", "goodbye", "string"};
	PrintArray(arr3, 3);
	std::cout << "Minimum: " << findMinimum(arr3, 3) << std::endl;
	std::cout << "Maximum: " << findMaximum(arr3, 3) << std::endl;
	std::cout << std::endl;

	return EXIT_SUCCESS;
}
