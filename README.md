# python_bubble_sort_performance
Using the Bubble Sort as a Performance Benchmark  

The Bubble Sort has value as an academic exercise, but its performance is poor for large lists and arrays.  

Unit testing demonstrates that the sort works properly. I coded the algorithm so that it can sort the incoming  
list or array in ascending (default) or descending order.  

Performance is reasonable up to about 1,000 elements. After that it trails off dramatically.  

I ran volume tests using randomly generated arrays of 10,000 integers.  

Numpy's np.sort() sorts a list of this size in about 2 thousanths of a second,  
an imperceptibly short amount of time to human perception.  

Despite my attempts to prevent the bubble sort to do any more work than it needed to,  
it took nearly 20 seconds to sort a list of 10,000 randomly generated integers.  

I expected the performance of the bubble sort to be worse, but I didn't expect it to be 10,000 times worse.  

There are a couple of caveats to consider. First, np.sort() is specifically designed to work with numpy arrays.  
It won't work with python lists. The Bubble Sort algorithm that I coded here will sort a list.  

The second caveat is that np.sort() probably runs as a compiled image rather than interpreted code.  
Python programs are interpreted. We expect them to run more slowly than a compiled C or C++ program.  

Despite the caveats, the performance difference is astonishing. Here is the log of the performance test.  

BEGIN PERFORMANCE TEST  

Test the NUMPY SORT with a randomly generated set of 10000 integers  
Note: np.sort() does not sort the array in place. It returns a sorted array.  

size of the array: 10000  
min value: 8  
max value: 99990  

first ten elements:  
[28782 68658 42103 83771 48256 10536  4454 93202 67185 69284]  
last ten elements:  
[71020 31926 69842  3598  1412 29009 92506 21030 70083 53474]  
sort using np.sort()  

*** NUMPY SORT completed ***  
Elapsed time: 0.00017879199913295452  

first ten elements:  
[  8  13  16  18  22  34  38  89 100 101]  
last ten elements:  
[99896 99907 99928 99932 99943 99944 99946 99982 99989 99990]  

Test the BUBBLE SORT with a randomly generated set of 10000 integers  
Note: As coded, the bubble sort algorithm sorts the array in place.  

size of the array: 10000  
min value: 2  
max value: 99979  

first ten elements:  
[ 3211 95249 64684 43616 77096 24959  3535 65660 29601 14387]  
last ten elements:  
[91673 85533 38729 39822 17538 90937 46401 45412  7145 32539]  

*** BUBBLE SORT completed ***  
Elapsed time: 19.966987682000763  

first ten elements:  
[  2  36  56  69  82  88  92 115 129 130]  
last ten elements:  
[99877 99879 99879 99879 99899 99935 99938 99939 99960 99979]  
END OF PERFORMANCE TEST  
