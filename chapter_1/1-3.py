pi_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
pi_str = pi_str.replace('.', '').replace(',', '')
ans = [len(word) for word in pi_str.split()]

print(ans)

