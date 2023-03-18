# Decorators
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    print(f'before yield = {word}')
    yield word
    print(f'after yield = {word}')

f = list(make_word())
print(f)