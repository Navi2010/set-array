import array as arr

my_array = arr.array('i', [1, 2, 3, 4, 3, 2])
print (my_array)

print('there are ' + str(my_array.count(2)) + ' 2s in this array.')

my_array.reverse()
print(my_array)