'''
We can use a nested for loop to obtain all the possible pairs in the list.

By using range(), we can make sure that the inner loop always starts one index ahead of the outer loop.

This removes the possibility of a comparison being repeated.
'''

def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False

num_list = [10, -14, 26, 5, -3, 13, -5]
print (check_sum(num_list))