from binary_search_tree import BSTNode
import time


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Replace the nested for loops below with your improvements
# O(n^2) time complexity
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# BST Solution: O(n log n) time complexity

t0 = time.time()
duplicates = []

popped_name = names_1.pop()
bst_names = BSTNode(popped_name)
for name in names_1:
    bst_names.insert(name)
for name in names_2:
    if bst_names.contains(name):
        duplicates.append(name)

t1 = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {t1 - t0} seconds")
print("\n***************************\n")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# Hash Table Solution: O(n) time complexity

t0 = time.time()
duplicates = []

hash_names = {popped_name: True}
for name in names_1:
    hash_names[name] = True
for name in names_2:
    if name in hash_names:
        duplicates.append(name)

t1 = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {t1 - t0} seconds")
