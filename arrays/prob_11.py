"""
Get Product of all other elements
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, if our input was [1,2,3,4,5], the expected output would be [120,60,40,30,24]. If our input was [3,2,1], the
expected output would be [2,3,6].
Follow up: What if you can't use division?
COMPLETED 6/8/19
"""
# Importing the timer
from daily_coding_problem.helper import timer

def multiplier(listo):
    '''
    Multiplies ever so simply!!
    :param listo:
    :return:
    '''
    product = 1
    for i in listo:
        product *= i

    return product


def prod_arr_create(listo):
    '''
    Gets the product of all numbers except for the indexed one, ya dig?
    :param listo:
    :return:
    '''
    # making a temp list clone to safely remove elements from and initialize final list
    temp_listo = listo[:]
    product_listo = list()

    # Iterating list, removing indexed element, then multiplying
    for i in range(len(listo)):
        del temp_listo[i]
        product_listo.append(multiplier(temp_listo))
        temp_listo = listo[:]

    return product_listo


@timer
def main():
    # put the array here
    array = [3,2,1]
    product_array = prod_arr_create(array)

    print(f'the product array is {product_array}')

    return


if __name__ == '__main__':
    main()