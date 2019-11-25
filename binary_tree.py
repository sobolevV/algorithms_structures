import random


class Node:
    stack = []

    def __init__(self, value=None):
        self.val = value
        self.left_node = None
        self.right_node = None

    def create_tree(self, values: list):
        self.val = values[0]
        for el in values[1:]:
            self.add_value(el)

    def add_value(self, value):
        if value < self.val:
            if self.left_node is not None:
                self.left_node.add_value(value)
            else:
                self.left_node = Node(value)
                self.stack.append(self.left_node)
                print(f"Parent - {self.val}, left - {value}")
        elif value > self.val:
            if self.right_node is not None:
                self.right_node.add_value(value)
            else:
                self.right_node = Node(value)
                self.stack.append(self.right_node)
                print(f"Parent - {self.val}, right - {value}")
        else:
            # print(f"exist - {value}")
            return

    def get_node_by_value(self, value, in_depth=True):
        """
        iterate nodes in stack
        :param value: find this value
        :param in_depth: flag to find in depth or width
        :return: node
        """
        for dep, sub_node in enumerate(self.stack if in_depth else self.stack.reverse()):
            if sub_node.val == value:
                print("depth :", dep + 1)
                return sub_node

    def get_left_node(self):
        if self.left_node is not None:
            return self.left_node.val
        return None

    def get_right_node(self):
        if self.right_node is not None:
            return self.right_node.val
        return None

    def get_tree_size(self):
        return len(self.stack)

    def print_node(self):
        print(f"Value : {self.val} \nHas left value: {self.get_left_node()} \n \
            Has right value: {self.get_right_node()}")


if __name__ == "__main__":
    arr = [random.randint(-100, 100) for value in range(100)]
    random_index = random.randint(0, 100)
    # init root
    tree = Node()
    # add random values
    tree.create_tree(arr)
    # get node by value
    rand_node = tree.get_node_by_value(arr[random_index])
    rand_node.print_node()
