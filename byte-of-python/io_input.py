#反转文字
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

sth = input("enter text: ")
if is_palindrome(sth):
    print("yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
