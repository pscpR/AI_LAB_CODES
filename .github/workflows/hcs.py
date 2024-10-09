import random

def HCS(f,neighbours_fn, max_iter = 1000):
    current = random.choice(list(x_range))
    print(current)
    for i in range(max_iter):
        neighbours = neighbours_fn(current)
        next_neighbours = max(neighbours, key = lambda x:f(x))
        if f(next_neighbours) <= f(current):
            break
        current = next_neighbours
    return (round(current),round(f(current)))



def f(x):
    return -x**2

def neighbours_fn(x):
    return [x + dx for dx in [-0.1,0,0.1]]

x_range = [x for x in range(10)]
print(HCS(f,neighbours_fn))
      