"""
Complete the code to pass all the test
"""

#####################################################################
# For Loops


def print_list(lst):
    """Prints out each item in a list.

    >>> lst = ["ant", "bear", "caterpillar"]
    >>> print_list(lst)
    ant
    bear
    caterpillar
    """

    for i in lst:
		print i


def print_even_0_to_20():
	for i in range(0,21,2):
		print i



#####################################################################
# While Loops

def count_down_20():
	count = 20
	while count > 0:
		print count
		count -= 1


#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
