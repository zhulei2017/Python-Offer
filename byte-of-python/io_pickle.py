import pickle
shoplistfile = 'shoplist.data'

shoplist =['aaa', 'bbb', 'ccc']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

