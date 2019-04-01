def total(a=5, *numbers, **phonebook):
    print('a', a)

    #遍历元祖中所有项目
    for single_item in numbers:
        print('single_item', single_item)

    #遍历词典中所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,2,3,4,jack=112,jhon=223,inge=1234))
