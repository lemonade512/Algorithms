/*
 * =====================================================================================
 *
 *       Filename:  test_array.cpp
 *
 *    Description:  Testing the Array class
 *
 *        Version:  1.0
 *        Created:  02/12/2015 10:07:50 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Phillip (), philliplemons512@gmail.com
 *   Organization:
 *
 * =====================================================================================
 */


#include "gtest/gtest.h"
#include "../../Algorithms/Arrays/C++/ArrayStats.h"

TEST(ArrayTest, test1) {
	int arr[] = {1,2,3,4,6,7,0};
	ASSERT_EQ(findMinimum(arr, 7), 0);
	ASSERT_EQ(findMaximum(arr, 7), 7);
	ASSERT_EQ(findAverage(arr, 7), 3);
	/*
	std::cout << "Sample Variance: " << findSampleVariance(arr, 7) << std::endl;
	std::cout << "Standard Deviation: " << findStdDeviation(arr, 7) << std::endl;
	std::cout << std::endl;
	*/
}

int main(int argc, char **argv) {
	  ::testing::InitGoogleTest(&argc, argv);
	    return RUN_ALL_TESTS();
}
