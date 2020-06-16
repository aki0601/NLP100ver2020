def n_gram(target, n):
      # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

x = 'paraparaparadise'
y = 'paragraph'

X = n_gram(x, 2)
Y = n_gram(y, 2)

xy_union = set(X) | set(Y)
print(xy_union)
xy_intersection = set(X) & set(Y)
print(xy_intersection)
xy_difference = set(X) - set(Y)
print(xy_difference)

print( 'se' in set(X) & set(Y))

# Ref. https://note.nkmk.me/python-list-common/