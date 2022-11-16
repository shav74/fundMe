import random
import time

# 2

data = [1, 2, 3, 4, 5, 12, 13, 17, 66]


def linear_search(target, items):
    for index in range(0, len(items)):
        if target == items[index]:
            return index
    return -1


# print("key found at position {}".format(linear_search(1,data)))

def binary_search(target, items):
    end = len(items) - 1
    start = 0
    key_found = 0
    while end >= start:
        middle = int((start + end) / 2)
        if target == items[middle]:
            return middle
            key_found = 1
        elif target > items[middle]:
            start = middle + 1
        else:
            end = middle - 1

    if key_found == 0:
        return -1


# key = binary_search(17,data)
# print("target found at index " + str(key))

# 2
# a
def get_random(size):
    a = []
    for i in range(0, size):
        a.append(random.randint(0, 100))
    return a


times_linear_search = []
for i in range(0, 11):
    start = time.time()
    linear_search(50, get_random(10000))
    end = time.time()
    times_linear_search.append(end - start)

print(times_linear_search)
print("max time is ", max(times_linear_search))

# 1k
start = time.time()
linear_search(50, get_random(1000))
end = time.time()
time_passed = end - start
print("time for 1k for linear search is ", time_passed)

# 5k

start = time.time()
linear_search(50, get_random(5000))
end = time.time()
time_passed = end - start
print("time for 5k linear search is ", time_passed)

# 10k

start = time.time()
linear_search(50, get_random(10000))
end = time.time()
time_passed = end - start
print("time for linear search 10k is ", time_passed)

# 50k

start = time.time()
linear_search(50, get_random(50000))
end = time.time()
time_passed = end - start
print("time for 50k linear search is ", time_passed)

# binary search

times_binary_serch = []
for i in range(0, 11):
    start = time.time()
    binary_search(50, get_random(10000))
    end = time.time()
    times_binary_serch.append(end - start)

print(times_binary_serch)
print("max time for binary search is ", max(times_binary_serch))

# 1k
start = time.time()
binary_search(50, get_random(1000))
end = time.time()
time_passed = end - start
print("time for 1k for bianry search is ", time_passed)

# 5k

start = time.time()
binary_search(50, get_random(5000))
end = time.time()
time_passed = end - start
print("time for 5k bianry search is ", time_passed)

# 10k

start = time.time()
binary_search(50, get_random(10000))
end = time.time()
time_passed = end - start
print("time for bianry search 10k is ", time_passed)

# 50k

start = time.time()
binary_search(50, get_random(50000))
end = time.time()
time_passed = end - start
print("time for 50k binary search is ", time_passed)


