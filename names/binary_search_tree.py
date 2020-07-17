"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # https://codereview.stackexchange.com/a/109410
    def __repr__(self):
        if self.right is not None:
            fmt = '{}({value!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({value!r}, {left!r})'
        else:
            fmt = '{}({value!r})'
        return fmt.format(type(self).__name__, **vars(self))

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is a node
        # if not, create the node and return
        if self is None:
            self = BSTNode(value)
            return self

        # if there is a node,
        # check if the value to insert is less than the current node's value
        if value < self.value:
            # if it is less than the current node's value,
            # check that there isn't a left child
            if self.left is None:
                # create the node here if there isn't a left child
                self.left = BSTNode(value)
            else:
                # call insert again if there is already a left child
                self.left.insert(value)
        else:
            # if the value is gte the current node's value,
            # check that there isn't a right child
            if self.right is None:
                # create the node here if there isn't a right child
                self.right = BSTNode(value)
            else:
                # call insert again if there is already a right child
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()
        q.append(self)

        while len(q) > 0:
            curr = q.popleft()
            print(curr.value)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [self]
        while len(stack) > 0:
            curr = stack.pop()
            print(curr.value)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)
