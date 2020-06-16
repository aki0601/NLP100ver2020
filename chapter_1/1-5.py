def n_gram(target, n):
      # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]


sentence = 'I am an NLPer'
for i in range(1, 4):
    print(n_gram(sentence, i))
    print(n_gram(sentence.split(' '), i))
