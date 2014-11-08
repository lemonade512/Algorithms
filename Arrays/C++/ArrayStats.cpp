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

template<typename Type>
Type findMinimum(Type arr[], int n)
{
	if (n == 0)
	{
		throw std::length_error("Can't find min of zero-length array");
	}

	Type min = arr[0];
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

int main ( int argc, char *argv[] )
{
	int arr[] = {1,2,3,4,6,7,0};
	PrintArray(arr, 7);
	std::cout << "Minimum: " << findMinimum(arr, 7) << std::endl;
	std::cout << "Maximum: " << findMaximum(arr, 7) << std::endl;
	int arr2[] = {6,2,3,4,6,7,49};
	PrintArray(arr2, 7);
	std::cout << "Minimum: " << findMinimum(arr2, 7) << std::endl;
	std::cout << "Maximum: " << findMaximum(arr2, 7) << std::endl;
	return EXIT_SUCCESS;
}
