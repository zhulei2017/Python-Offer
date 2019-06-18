def reverse_words(sentence):
    tmp = sentence.split()
    return ' '.join(tmp[::-1])


if __name__=="__main__":
    test = 'I am a student.'
    print(reverse_words(test))
