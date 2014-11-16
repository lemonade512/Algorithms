/*
 * =====================================================================================
 *
 *       Filename:  IndexOf.cpp
 *
 *    Description:  Holds a function to find the index of an item.
 *
 *        Version:  1.0
 *        Created:  11/08/2014 08:27:15 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Phillip (), philliplemons512@gmail.com
 *   Organization:
 *
 * =====================================================================================
 */


#include	<stdlib.h>
#include    <string>
#include    <stdio.h>
#include    <iostream>

// TODO move this to a utils file (also move the one in ArrayStats)
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
int indexOf(T arr[], int n, T val)
{
	for (int i = 0; i < n; i++)
	{
		if (arr[i] == val)
		{
			return i;
		}
	}

	return -1;
}

int main ( int argc, char *argv[] )
{
	int arr1[] = {0, 1, 2, 5, 8};
	PrintArray(arr1, 5);
	std::cout << "Index of 5: " << indexOf(arr1, 5, 5);
	return EXIT_SUCCESS;
}
