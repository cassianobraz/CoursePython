#  shallow copy
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2]
}

d2 = copy.deepcopy(d1)
d2['li'][1] = 9999
print(d1)
print(d2)
