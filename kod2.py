# lst = [10, 20, 30, 40, 50]
# dbl_lst = [i * 2 for i in lst]
    
# print("Original lst:", lst)
# print("List:", dbl_lst)


# names =['John', 'alex', 'catherine', 'bob', 'eve']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

nested_list =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)