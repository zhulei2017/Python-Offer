def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


print_links([1,2,3])
