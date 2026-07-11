import itertools

def find_combinations(items, r):
    return list(itertools.combinations(items, r))

if __name__ == '__main__':
    items = ['A', 'B', 'C', 'D']
    combos = find_combinations(items, 2)
    print(f'Combinations of {items} taken 2 at a time:')
    for c in combos:
        print(c)