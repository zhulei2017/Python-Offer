ab = {
    'swaroop':'swaroop@11.com',
    'asd':'asd@22.com'
}

print('swaroop address is', ab['swaroop'])

for name, address in ab.items():
    print('contact {} at {}'.format(name, address))

ab['qwe'] = 'qwe@qq.com'

if 'qwe' in ab:
    print("\nqwe's address is", ab['qwe'])
