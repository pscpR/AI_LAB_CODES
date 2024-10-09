import itertools

def get_value(word,substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve(equation):
    left,right = equation.lower().replace(" ","").split('=')
    l = left.split("+")
    letters = set(right)
    for word in l:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    print(left)
    digits = range(10)
    for permutations in itertools.permutations(digits,len(letters)):
        sol = dict(zip(letters,permutations))
        if sum(get_value(word,sol) for word in l) == get_value(right,sol):
            print("+".join(str(get_value(word, sol)) for word in l) + " = {} (mapping: {})".format(get_value(right, sol), sol))




solve('SEND + MORE = MONEY')