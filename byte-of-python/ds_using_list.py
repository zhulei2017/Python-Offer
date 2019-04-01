#this is a list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('i have {} items to purchase'.format(len(shoplist)))

print('these items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\ni also hace to bur rice.')
shoplist.append('rice')
print('my shopping list is now', shoplist)

print('i will sort my list now')
shoplist.sort()
print('sorted list is ', shoplist)

print('the first to buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i bought the', olditem)
print('my shopping list is now',shoplist)
