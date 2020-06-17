def cipher(text):
    result = ''
    for word in text:
        if word.islower():
            result += chr(219 - ord(word))
        else:
            result += word
    return result

x = 'This is Test text 12345'
print(cipher(x))

# Ref. https://hibiki-press.tech/python/isupper-islower/3728#toc3
# Ref. 