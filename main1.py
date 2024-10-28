setx = {'blue', 'light blue', 'black', 'light purple'}
sety = {'white', 'blue', 'navy blue', 'dark blue'}

uni = setx.union(sety)
print('the joined answer is: ', uni)

inter = setx.intersection(sety)
print('the common things is/are: ', inter)

dif = setx.difference(sety)
print('the answer is: ', dif)

sym = setx.symmetric_difference(sety)
print(sym)