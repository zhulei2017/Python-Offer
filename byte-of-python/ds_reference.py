print('simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del mylist[0]

print('shoplist is', shoplist)
print('my list is', mylist)

print('copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
