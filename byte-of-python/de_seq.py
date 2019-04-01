shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('item 1 is', shoplist[1])
print('item -1 is', shoplist[-1])
print('item -2 is', shoplist[-2])
print('character 0 is', name[0])
print('character 0 is', name[1])
print('character 0 is', name[-1])

#slicing
print('item 1 to -1 is', shoplist[1:-1])
print('item -1 to 1 is ', shoplist[-1:1])
print('item 2 to end is', shoplist[2:])
print('item start to end is', shoplist[:])

print(shoplist[::-1])
