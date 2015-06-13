/*
 * =====================================================================================
 *
 *       Filename:  ArrayStats.h
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  06/13/2015 12:39:15 PM
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
