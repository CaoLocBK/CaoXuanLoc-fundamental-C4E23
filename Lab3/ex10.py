from ex9 import get_even_list

even_list = get_even_list([1,2,-3,4])
if set(even_list) == set([2,4]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")