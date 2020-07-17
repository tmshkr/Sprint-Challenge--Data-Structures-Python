class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        next_node = "None" if self.next_node is None else f"{self.next_node.value} at {hex(id(self.next_node))}"
        return f"<Node\n  value: {self.value} at {hex(id(self))}\n  next_node: {next_node}\n>"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        string = ""
        while curr:
            string += str(curr) + "\n"
            curr = curr.next_node
        return string

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # Recursive solution: O(n) time complexity
    def reverse_list(self, node, prev):
        if node is None:
            self.head = prev
            return

        next_node = node.next_node
        node.next_node = prev
        self.reverse_list(next_node, node)


ll = LinkedList()
ll.add_to_head(5)
ll.add_to_head(4)
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)
