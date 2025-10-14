#  Complexidade log(n)
def search_binary(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        halfway = (low + high) // 2
        kick = list[halfway]

        if kick == item:
            return halfway
        elif kick < item:
            return halfway + 1
        else:
            high = halfway - 1

    return None


list = [1, 2, 3, 10, 20, 30, 34, 36, 40, 41, 222, 300, 540, 1000]
target = 2
index = search_binary(list, target)
print(index)
