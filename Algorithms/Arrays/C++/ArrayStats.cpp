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
#include "ArrayStats.h"

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
