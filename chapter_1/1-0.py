a = "stressed"
conv  = ''.join(list(reversed(a)))
print(conv)

# Ref. https://note.nkmk.me/python-reverse-reversed/

# よりスマートな方法
conv2 = a[::-1]
print(conv2)

