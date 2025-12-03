data_none = None
data_bool = True
data_int = 24
data_float = 3.4
data_complex = 3+4j
data_str = "hello"
data_byte = b"\x41\x32\x42"


# print(data_none)
# print(data_bool)
# print(data_byte)

bool_methods_lst = dir(data_bool)


# print(bool_methods_lst)
# print(type(bool_methods_lst))


my_list = [1, 2, 4, 5, 6]
my_list2 = [1, 'a', True]


# print(my_list)
# print(my_list2)

my_set = {1, 2, 2, 4}

my_dict = {'length': [1.0, 2.3, 4, 5, 6], 'width': [1.0, [2.3], {4, 5}, 6]}

print(dir(my_dict))

print(list(my_dict.values()))

my_tuple = (2, 3)

# print(my_set)
# print(my_dict)
# print(my_tuple)

# print(dir(my_list))
# print(my_list.__doc__)

my_list.append('a')

my_list2 = my_list

my_list_copy = list(my_list)

my_list2.append('b')
my_list_copy.append('c')

# print(id(my_list))
# print(id(my_list2))
# print(id(my_list_copy))

# print(my_list)
# print(my_list2)
# print(my_list_copy)

list_gen = [x**2 for x in range(0,5)]

# print(list_gen)

point_list = [3.5, 6.4, 7.0, 6]

# print(min(point_list))
# print(max(point_list))
# print(sum(point_list))
# print(sum(point_list)/len(point_list))

# print(len(my_list))
# print(my_list)

my_list.extend(['x','y','z'])

my_list.reverse()

# print(my_list)

################## set ##############


my_set = set([1, 2, 3])

my_set = {1, 2, 3}

# print(type(my_set))
# print(my_set)

my_set.update([3, 4], [2, 6])

# print(my_set)

a_set = {2, 3, 5}
b_set = {9, 1, 3, 5}
c_set = {7, 4, 8}

u_set = a_set.symmetric_difference(b_set)

# print(u_set)

# print(a_set<b_set)


s = "asdfdfs"
s2 = "asdfdfs".capitalize()
print(id(s))
print(id(s2))
print(s[2])