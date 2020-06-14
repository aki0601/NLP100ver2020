elements = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
elements = elements.replace('.','')
idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
for i,word in enumerate(elements.split(),1):
    if i in idx:
        l = word[:1]
    else:
        l = word[:2]
    dic[l] = i
print (dic)

# Ref. https://note.nkmk.me/python-enumerate-start/